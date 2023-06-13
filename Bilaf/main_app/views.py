from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import User

# Create your views here.
def home_page(request: HttpRequest):

    return render(request, 'main_app/home_page.html')

