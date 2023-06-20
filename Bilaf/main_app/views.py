from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from users_app.models import Store
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User , Permission, Group
import plotly.express as px
from .models import Product,Categories,Review,Cart,CartItem
from django.core.mail import send_mail,EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()  



# import io
# import urllib
# import base64
# import matplotlib.pyplot as plt



# Create your views here.
def home_page(request: HttpRequest):
    categories = Categories.objects.all()
    all_store_categories = [choice[0] for choice in Store.CHOICES]
    stores = Store.objects.all()
    products = Product.objects.all()
    return render(request, 'main_app/home_page.html', {"categories":categories,"all_store_categories":all_store_categories , "stores":stores, "proudcts":products})

def base_page(request: HttpRequest):
    return render(request, "main_app/base.html")


def add_page(request: HttpRequest):
    return render(request, "main_app/add_product.html")


def check_out(request: HttpRequest):
    return render(request, "main_app/check_out.html")


def product_details(request: HttpRequest):
    return render(request, "main_app/product_details.html")


def shoping_cart(request: HttpRequest):


    return render(request, "main_app/shoping_cart.html")


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
    products = Product.objects.all()
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

    products = Product.objects.get(id = product_id)
    categories = Categories.objects.get(name = products.category.name)
    store = Store.objects.get(store_name = products.store.store_name)
    return render(request, 'main_app/product_details.html', {'products':products,"categories":categories,"store":store})
   
def catgory_page(request: HttpRequest):
    categories = Categories.objects.all()
    return render(request, "main_app/catgory_page.html", {"categories": categories})


def store_page(request: HttpRequest):
    Category = Categories.objects.all()
    stores = Store.objects.all()
    return render(request, 'main_app/store_page.html', {'stores': stores})

def store_pages_filtered_based_on_category(request: HttpRequest, categories_id):
    Category = Categories.objects.get(id = categories_id)
    stores = Store.objects.filter(category = Category)
    return render(request, 'main_app/store_page.html', {'stores': stores})
     
def merchant_dashboard_view(request:HttpRequest):
    store = Store.objects.get(owner = request.user)
    products = Product.objects.filter(store = store).all()
    product_names = []
    product_quantities = []
    for product in products:
        product_names.append(product.name)
        product_quantities.append(product.quantity)
    fig = px.bar(x=product_names, y=product_quantities, labels={'x': 'Products', 'y':'Quantities'})
    graph = fig.to_html(full_html=False, default_height=500, default_width=700)
    return render(
        request,
        "main_app/dashboard.html",
        {"products": products, "graph":graph},
    )

     
     
@login_required(login_url={"/users_app/login/"}) 
def user_adding_review(request:HttpRequest, product_id):
    if request.user.groups.filter(name='costumer').exists():
        if request.method == "POST":
            user_instance = request.user
            status = Cart.objects.get(customer = user_instance)
            if status.is_active: 
                product_object = Product.objects.get(id = product_id)
                comment = request.POST["comment"]
                pass


@login_required(login_url={"/users_app/login/"})
def delete_product(request:HttpRequest, product_id):

    products = Product.objects.get(id = product_id)
    products.delete()
    return redirect("main_app:product_page") 
   
@login_required(login_url={"/users_app/login/"})
def update_product(request:HttpRequest, product_id):

    products = Product.objects.get(id=product_id)
    #updating the product
    if request.method == "POST":
        products.category = request.POST["category"]
        products.price = float(request.POST["price"]),
        products.name = request.POST["name"],
        products.quantity = int(request.POST["quantity"]),
        products.description = request.POST["description"],
        products.image=  request.POST["image"]
        products.save()


        return redirect("main_app:product_detail", products_id=products.id)

    return render(request, 'main_app/update_product.html', {"products" : products})  

@login_required(login_url={"/users_app/login/"})
def delete_catgory(request:HttpRequest, categories_id):

    categories = Categories.objects.get(id =categories_id)
    categories.delete()
    return redirect("main_app:catgory_page")   


@login_required(login_url={"/users_app/login/"})
def update_catgory(request:HttpRequest, categories_id):

    categories = Categories.objects.get(id=categories_id)
    #updating the catgory
    if request.method == "POST":
        categories.logo = request.POST["logo"]
        categories.name = request.POST["name"],
        categories.save()


        return redirect("main_app:product_detail", categories_id=categories.id)

    return render(request, 'main_app/update_catgory.html', {'categories': categories})


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

def order_status(request: HttpRequest):
    return render(request, "main_app/order_status.html")
def view_order(request: HttpRequest):
    return render(request, "main_app/view_order.html")

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