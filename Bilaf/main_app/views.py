from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from users_app.models import Store
from django.contrib.auth.decorators import login_required
from .models import Product



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

@login_required(login_url={"users_app:login"})
def add_product(request:HttpRequest, store_id):
    if request.user.groups == "merchant":
        if request.method == "POST":
            store_object = Store.objects.filter(id = store_id)
            price = request.POST["price"],
            name = request.POST["name"],
            description = request.POST["description"]
            if "image" in request.FILES:
                image = request.FILES["image"]
                
            new_product = Product(
                store_object,
                price,
                name,
                description,
                image     
            )
        new_product.save() 
    else:
        redirect("users_app:no_permission_page")      
    return render(request, "main_app/add_product.html")