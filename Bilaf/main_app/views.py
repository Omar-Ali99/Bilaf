from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


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

def contect_us(request: HttpRequest):

    return render(request, 'main_app/contact_us.html')



    
