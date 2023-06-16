from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.
def home_page(request: HttpRequest):

    return render(request, 'main_app/home_page.html')

def base_page(request: HttpRequest):

    return render(request, 'main_app/base.html')

    
def add_page(request: HttpRequest):

    return render(request, 'main_app/add_product.html')

    
