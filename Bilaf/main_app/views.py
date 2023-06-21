from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpRequest, HttpResponse
from users_app.models import Store
from django.contrib.auth.decorators import login_required
from .models import Product,Categories,Review,Cart,CartItem
from django.contrib.auth.models import User , Permission, Group
from django.db.models import F, Sum
from django.core.mail import send_mail,EmailMessage
from dotenv import load_dotenv
import os

load_dotenv() 






# Create your views here.
def home_page(request: HttpRequest):
    categories = Categories.objects.all()
    all_store_categories = [choice[0] for choice in Store.CHOICES]
    stores = Store.objects.all()
    products = Product.objects.all()
    return render(request, 'main_app/home_page.html', {"categories":categories,"all_store_categories":all_store_categories , "stores":stores, "products":products})

def base_page(request: HttpRequest):
    return render(request, "main_app/base.html")


def add_page(request: HttpRequest):
    return render(request, "main_app/add_product.html")


def check_out(request: HttpRequest):
    return render(request, "main_app/check_out.html")


def product_details(request: HttpRequest):
    return render(request, "main_app/product_details.html")


def about_us(request: HttpRequest):
    return render(request, "main_app/about_us.html")


def about_project(request: HttpRequest):
    return render(request, "main_app/about_project.html")


def pick_delv_policies(request: HttpRequest):
    return render(request, "main_app/pickup_delivery_policy.html")


def search(request: HttpRequest):
    search_phrase = request.GET.get("search", "")
    selected_filter = request.GET.get('filter')
    filtered_data = Store.objects.all()

    if selected_filter:
        filtered_data = filtered_data.filter(category=selected_filter)

    stores = Store.objects.filter(store_name__icontains=search_phrase)

    if selected_filter:
        stores = stores.filter(category=selected_filter)

    context = {
        'filtered_data': filtered_data,
        'selected_filter': selected_filter,
        'stores': stores,
        'search_phrase':search_phrase,
    }

    return render(request, 'main_app/search.html', context)


@login_required(login_url={"/users_app/login/"})
def merchant_adding_categories(request: HttpRequest):
    if not request.user.groups.filter(name="merchant").exists():
        return redirect("users_app:no_permission_page")

    msg = None

    if request.method == "POST":
        if "logo" in request.FILES:
            new_logo = request.FILES["logo"]

        new_category = Categories(
            name=request.POST["name"],
            store=Store.objects.get(owner=request.user),
            logo=new_logo,
        )

        try:
            new_category.save()
            msg = "Category added successfully"
        except Exception as e:
            print(e)

    return render(request, "main_app/add_categories.html", {"msg": msg})



@login_required(login_url={"/users_app/login/"})
def merchant_adding_products(request: HttpRequest):
    msg = None
    store_object = Store.objects.get(owner = request.user)
    if Categories.objects.filter(store = store_object):
        if request.user.groups.filter(name='merchant').exists():
            categories_object = Categories.objects.filter(store=store_object)
            if request.method == "POST":
                image_instance = None
                if "image" in request.FILES:
                    image_instance = request.FILES["image"]

                category_instance = Categories.objects.get(id=request.POST["category"])

                new_product = Product(
                    store=Store.objects.get(owner=request.user),
                    category=category_instance,
                    price=float(request.POST["price"]),
                    name=request.POST["name"],
                    quantity=int(request.POST["quantity"]),
                    description=request.POST["description"],
                    image=image_instance,
                )

                try:
                    new_product.save()
                    msg = "Product added successfully"
                except Exception as e:
                    print(e)

                return render(request,"main_app/add_product.html",{"categories": categories_object, "msg": msg, "category_instance":category_instance},
                )
            else:
                return render(request,"main_app/add_product.html",{"categories": categories_object},
                )
        else:
            return redirect("users_app:no_permission_page")
    else:
        return redirect("main_app:add_categories")


def product_page(request: HttpRequest):
    product_store = Store.objects.filter(owner= request.user)
    products = Product.objects.filter(store__in=product_store)
    return render(request, "main_app/product_page.html", {"products": products})


def product_detail(request: HttpRequest, product_id):

    products = Product.objects.get(id=product_id)
    product_store = products.store
    customer_cart = Cart.objects.filter(customer=request.user, status="Pending")
    warning = False

    if customer_cart.exists():
        if customer_cart.first().store != product_store:
            warning = True

    return render(
        request,
        "main_app/product_details.html",
        {"products": products, "warning": warning},
    )


def catgory_page(request: HttpRequest):
    categories = Categories.objects.all()
    return render(request, "main_app/catgory_page.html", {"categories": categories})


def merchent_store_page(request: HttpRequest):
    Category = Categories.objects.all()
    stores = Store.objects.all()
    return render(request, 'main_app/store_page.html', {'stores': stores})
     
def dashboard_view(request: HttpRequest):
    store = Store.objects.get(owner=request.user)

    products = Product.objects.filter(store=store)
    categories = Categories.objects.filter(store=store)

    done_carts = Cart.objects.filter(store=store, status="Done")
    cart_items_in_done_carts = CartItem.objects.filter(cart__in=done_carts)

    unique_customers_count = done_carts.values("customer").distinct().count()

    for product in products:
        sold_cart_items = cart_items_in_done_carts.filter(product=product)

        product.total_earnings = sum(
            cart_item.quantity * cart_item.price for cart_item in sold_cart_items
        )

        product.total_sold_units = sum(
            cart_item.quantity for cart_item in sold_cart_items
        )

    product_total_earnings = sum(product.total_earnings for product in products)
    product_total_units_sold = sum(product.total_sold_units for product in products)

    for category in categories:
        sold_cart_items = cart_items_in_done_carts.filter(product__category=category)

        category.total_earnings = sum(
            cart_item.quantity * cart_item.price for cart_item in sold_cart_items
        )

        category.total_sold_units = sum(
            cart_item.quantity for cart_item in sold_cart_items
        )

    category_total_earnings = sum(category.total_earnings for category in categories)

    category_total_units_sold = sum(
        category.total_sold_units for category in categories
    )

    return render(
        request,
        "main_app/dashboard.html",
        {
            "products": products,
            "categories": categories,
            "served_orders": done_carts,
            "unique_customers": unique_customers_count,
            "product_total_earnings": product_total_earnings,
            "product_total_units_sold": product_total_units_sold,
            "category_total_earnings": category_total_earnings,
            "category_total_units_sold": category_total_units_sold,
        },
    )

    return render(
        request,
        "main_app/dashboard.html",
        {"products": products, "categories": categories},
    )


@login_required(login_url={"/users_app/login/"})
def user_adding_review(request: HttpRequest, product_id):
    if request.user.groups.filter(name="costumer").exists():
        if request.method == "POST":
            user_instance = request.user
            status = Cart.objects.get(customer=user_instance)
            if status.is_active:
                product_object = Product.objects.get(id=product_id)
                comment = request.POST["comment"]
                pass


@login_required(login_url={"/users_app/login/"})
def delete_product(request: HttpRequest, product_id):
    products = Product.objects.get(id=product_id)
    products.delete()
    return redirect("main_app:product_page")


@login_required(login_url={"/users_app/login/"})
def update_product(request: HttpRequest, product_id):
    products = Product.objects.get(id=product_id)
    # updating the product
    if request.method == "POST":
        products.category = request.POST["category"]
        products.price = (float(request.POST["price"]),)
        products.name = (request.POST["name"],)
        products.quantity = (int(request.POST["quantity"]),)
        products.description = (request.POST["description"],)
        products.image = request.POST["image"]
        products.save()

        return redirect("main_app:product_detail", products_id=products.id)

    return render(request, "main_app/update_product.html", {"products": products})


@login_required(login_url={"/users_app/login/"})
def delete_catgory(request: HttpRequest, categories_id):
    categories = Categories.objects.get(id=categories_id)
    categories.delete()
    return redirect("main_app:catgory_page")


@login_required(login_url={"/users_app/login/"})
def update_catgory(request: HttpRequest, categories_id):
    categories = Categories.objects.get(id=categories_id)
    # updating the catgory
    if request.method == "POST":
        categories.logo = request.POST["logo"]
        categories.name = (request.POST["name"],)
        categories.save()

        return redirect("main_app:product_detail", categories_id=categories.id)

    return render(request, "main_app/update_catgory.html", {"categories": categories})


@login_required(login_url={"/users_app/login/"})
def add_to_cart(request: HttpRequest):
    if request.method != "POST":
        return redirect("users_app:no_permission_page")

    product_object = Product.objects.get(id=request.POST["product_id"])
    product_store = product_object.store
    try:
        customer_cart = Cart.objects.get(customer=request.user, status="Pending")
    except:
        customer_cart = None
    quantity = int(request.POST["quantity"])
    user = request.user

    if customer_cart is not None:
        if customer_cart.store == product_store:
            create_cart_item(quantity, product_object, customer_cart)
        else:
            customer_cart.delete()
            customer_cart = create_new_cart(user, product_store)
            create_cart_item(quantity, product_object, customer_cart)
    else:
        new_cart = create_new_cart(user, product_store)
        create_cart_item(quantity, product_object, new_cart)

    return redirect("main_app:cart")


def create_new_cart(user: User, product_store: Store):
    new_cart = Cart(
        store=product_store,
        customer=user,
        status="Pending",
        due_date=None,
    )
    new_cart.save()

    return new_cart


def create_cart_item(quantity: int, product_object: Product, customer_cart: Cart):
    cart_item = CartItem(
        cart=customer_cart,
        product=product_object,
        quantity=quantity,
    )
    cart_item.save()

@login_required(login_url={"/users_app/login/"})
def shoping_cart(request: HttpRequest):
    msg = None
    customer_cart = Cart.objects.filter(customer=request.user, status="Pending")
    if customer_cart.exists():
        cart_items = CartItem.objects.filter(cart__in=customer_cart)
        delivery_options = {
            "pick_up": customer_cart.first().store.pick_up_enabled,
            "delivery": customer_cart.first().store.delivery_enabled,
        }
        cart_total = calculate_total(customer_cart, is_cart=True)
        return render(
            request,
            "main_app/shoping_cart.html",
            {
                "msg": msg,
                "cart": customer_cart,
                "cart_items": cart_items,
                "cart_total": cart_total,
                "delivery_options": delivery_options,
            },
        )
    else:
        msg = "Your Cart is empty"
        return render(request, "main_app/shoping_cart.html", {"msg": msg})


def calculate_total(customer_cart: Cart, is_cart: bool = False):
    if is_cart:
        cart_total = (
            CartItem.objects.filter(cart__in=customer_cart)
            .annotate(item_total=F("product__price") * F("quantity"))
            .aggregate(total=Sum("item_total"))["total"]
            or 0
        )
    else:
        cart_total = (
            CartItem.objects.filter(cart=customer_cart)
            .annotate(item_total=F("price") * F("quantity"))
            .aggregate(total=Sum("item_total"))["total"]
            or 0
        )

    return cart_total


def orders(request: HttpRequest):
    user = Store.objects.get(owner=request.user)
    orders = Cart.objects.filter(store=user).exclude(status="Pending")
    orders_prices = {}
    for order in orders:
        total_price = calculate_total(order)
        orders_prices[order.id] = total_price
    print(orders_prices)
    return render(
        request,
        "main_app/orders.html",
        {"orders": orders, "orders_prices": orders_prices},
    )


@login_required(login_url="/users/login/")
def view_order(request: HttpRequest, cart_id):
    order = Cart.objects.get(id=cart_id)
    if order.store.owner != request.user:
        return redirect("users_app:no_permission_page")
    else:
        items = CartItem.objects.filter(cart=order)
        total_price = calculate_total(order)
        return render(
            request,
            "main_app/view_order.html",
            {"order": order, "items": items, "total_price": total_price},
        )


@login_required(login_url="/users/login/")
def place_order(request: HttpRequest):
    print("first")
    if request.method == "POST":
        customer_cart = Cart.objects.filter(
            customer=request.user, status="Pending"
        ).first()
        cart_items = CartItem.objects.filter(cart=customer_cart)
        print(customer_cart)
        for cart_item in cart_items:
            print("for")
            cart_item.price = cart_item.product.price
            print(f"item: {cart_item.price} product: {cart_item.product.price}")
            cart_item.save()

        if customer_cart:
            print("if")
            customer_cart.status = "Submited"
            customer_cart.payment_option = request.POST["payment_option"]
            customer_cart.delivery_option = request.POST["delivery_option"]
            print(request.POST["payment_option"])
            print(request.POST["delivery_option"])
            customer_cart.save()
            print(customer_cart.status)
        return redirect("main_app:cart")
    else:
        return redirect("users_app:no_permission_page")


@login_required(login_url="/users/login/")
def update_cart(request: HttpRequest):
    customer_cart = Cart.objects.filter(customer=request.user, status="Pending")
    if customer_cart.exists():
        cart_items = CartItem.objects.filter(cart__in=customer_cart)
        for item in cart_items:
            id = str(item.id)
            CartItem.objects.filter(id=item.id).update(quantity=request.POST[f"{id}"])

    return redirect("main_app:cart")


@login_required(login_url="/users/login/")
def delete_cart_item(request: HttpRequest, cart_item):
    customer_cart = Cart.objects.filter(customer=request.user, status="Pending")
    cart_items = CartItem.objects.filter(cart__in=customer_cart)
    if cart_items == 1:
        customer_cart.delete()
        return redirect("main_app:cart")
    else:
        cart_items.filter(id=cart_item).delete()
        return redirect("main_app:cart")


@login_required(login_url="/users/login/")
def order_action(request: HttpRequest, action: str, cart_id):
    try:
        print(cart_id)
        print(type(cart_id))
        cart = Cart.objects.get(id=int(cart_id))
        if cart.store.owner != request.user:
            return redirect("users_app:no_permission_page")
    except:
        print("None exist")
        return redirect("users_app:no_permission_page")
    if action == "Accept":
        cart.status = "Active"
        cart.save()
    elif action == "Decline":
        cart.status = "Declined"
        cart.save()
    elif action == "Done":
        cart.status = "Done"
        cart.save()
    else:
        print("wrong action")
        return redirect("users_app:no_permission_page")

    return redirect("main_app:orders_status")


def custom_404_view(request, exception):
    return render(request, "main_app/404.html", status=404)


def send_email(receiver:str, subject:str, message:str):
    function_subject = subject
    function_message = message
    function_mail_receiver = receiver
    from_email = os.getenv("DEFAULT_FROM_EMAIL")
    recipient_list = [function_mail_receiver]
    email = EmailMessage(
        function_subject,
        function_message,
        from_email,
        recipient_list,
        reply_to=[from_email],
    )
    try:
        email.send()
        return True
    except Exception:
        return False

#send_email('omar.ali99@live.com', 'Order Confirmation', 'Thank you for your order!')


def thanks_order_page(request: HttpRequest):
    return render(request, "main_app/Thanks_order_page.html")