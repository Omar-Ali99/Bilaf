from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from users_app.models import Store
from django.contrib.auth.decorators import login_required
from .models import Product,Categories,Review,Cart
from django.contrib.auth.models import User , Permission, Group
import io
import urllib
import base64
import matplotlib.pyplot as plt





# Create your views here.
def home_page(request: HttpRequest):

    return render(request, 'main_app/home_page.html')

def base_page(request: HttpRequest):

    return render(request, 'main_app/base.html')

    
def add_page(request: HttpRequest):

    return render(request, 'main_app/add_product.html')


def check_out(request: HttpRequest):

    return render(request, 'main_app/check_out.html')


def product_details(request: HttpRequest):

    return render(request, 'main_app/product_details.html')


def shoping_cart(request: HttpRequest):

    return render(request, 'main_app/shoping_cart.html')

def about_us(request : HttpRequest):
    return render(request, 'main_app/about_us.html')


def about_project(request : HttpRequest):
    return render(request, 'main_app/about_project.html')

def pick_delv_policies(request : HttpRequest):
    return render(request, 'main_app/pickup_delivery_policy.html')

def search(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    store = Store.objects.filter(store_name__icontains = search_phrase) or Store.objects.filter(category__icontains = search_phrase)

    selected_filter = request.GET.get('filter')  # Get the selected filter value from the request
    filtered_data = Store.objects.all()  # Fetch all data initially
    
    if selected_filter:
        filtered_data = filtered_data.filter(category=selected_filter)  # Apply filter based on selected value
        
    context = {
        'filtered_data': filtered_data,
        'selected_filter': selected_filter,
        'store': store,
    }
    
    return render(request, 'main_app/search.html', context)

@login_required(login_url={"/users_app/login/"})
def add_categories(request:HttpRequest):
    msg = None

    if request.user.groups.filter(name='merchant').exists():
            msg = None
            if request.method == "POST":
                if "logo" in request.FILES:
                    new_logo = request.FILES["logo"]
                
                new_category = Categories(
                name = request.POST["name"],
                store = Store.objects.get(owner=request.user),
                logo = new_logo
                )
                try:    
                    new_category.save()
                    msg = "Category added successfully"
                except Exception as e:
                    print(e)

    else:
        return redirect("users_app:no_permission_page") 
            
    return render(request, "main_app/add_categories.html", {"msg":msg})

           


@login_required(login_url={"/users_app/login/"})
def add_product(request:HttpRequest):
    msg = None
    if Categories.objects.get():
        if request.user.groups.filter(name='merchant').exists():
            store_object = Store.objects.get(owner = request.user)
            categories_object = Categories.objects.filter(store = store_object)
            if request.method == "POST":
                if "image" in request.FILES:
                    image_instance = request.FILES["image"]
                category_instance = Categories.objects.get(id = request.POST["category"])

                new_product = Product(
                    store = Store.objects.get(owner = request.user),
                    category = category_instance,
                    price = float(request.POST["price"]),
                    name = request.POST["name"],
                    quantity = int(request.POST["quantity"]),
                    description = request.POST["description"],
                    image= image_instance     
                )
                try:    
                    new_product.save()
                    msg = "Category added successfully"
                except Exception as e:
                    print(e)

                return render(request, "main_app/add_product.html", {"categories":categories_object, "msg":msg})
            else:
                return render(request, "main_app/add_product.html", {"categories":categories_object})
        else:
            return redirect("users_app:no_permission_page")  
    else:
        return redirect("main_app:add_categories") 
    


def dashboard_view(request:HttpRequest):
    store = Store.objects.get(owner = request.user)
    products = Product.objects.filter(store = store)
    categories = Categories.objects.filter(store = store)

    return render(request, 'main_app/dashboard.html', {"products":products, "categories":categories})

     
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