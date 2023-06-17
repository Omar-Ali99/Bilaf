from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile,Store,Product
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request: HttpRequest):
    if request.method == "POST":
        print(request.POST["phone"])
        try:
            new_user = User.objects.create_user(
                username=request.POST["user_name"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                password=request.POST["password"],
            )
            new_user.save()
            profile = Profile(user=new_user, phone_number=request.POST["phone"])
            profile.save()
            return redirect("main_app:home_page")
        except:
            print("error")
            msg = "Username taken!"
    return render(request, "users_app/login.html")


def login_page(request: HttpRequest):
    if request.user.is_authenticated:
        print(request.user.username)
        return redirect("main_app:home_page")
    # if user login already redirect to home page

    msg = None
    if request.method == "POST":
        user: User = authenticate(
            request,
            username=request.POST["user_name"],
            password=request.POST["password"],
        )
        if user:
            login(request, user)
            return redirect("main_app:home_page")
        else:
            msg = "Incorrect Credentials"

    return render(request, "users_app/login.html", {"msg": msg})


def signout_page(request: HttpRequest):
    logout(request)

    return redirect("main_app:home_page")


def no_permission_page(request: HttpRequest):
    return render(request, "users_app/no_permission.html")

@login_required(login_url={"users_app:login"})
def add_store(request:HttpRequest, Store_id):
    if request.user.is_merhcant:
        if request.method == "POST":
            store_object = Store.objects.filter(id = Store_id)
            new_product = Product(
                store_object,
                price = request.POST["price"],
                name = request.POST["name"],
                description = request.POST["description"]
            )
        new_product.save()       
    return render(request, "main_app/merchant_add.html")


@login_required(login_url={"users_app:login"})
def add_product(request:HttpRequest, Store_id):
    if request.user.is_merhcant:
        if request.method == "POST":
            store_object = Store.objects.filter(id = Store_id)
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
    return render(request, "main_app/merchant_add.html")