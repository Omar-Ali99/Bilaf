from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


# Create your views here.
def home_page(request: HttpRequest):

    return render(request, 'main_app/home_page.html')

def base_page(request: HttpRequest):

    return render(request, 'main_app/base.html')

def about_us(request : HttpRequest):
    return render(request, 'main_app/about_us.html')


def about_project(request : HttpRequest):
    return render(request, 'main_app/about_project.html')

def pick_delv_policies(request : HttpRequest):
    return render(request, 'main_app/pickup_delivery_policy.html')
