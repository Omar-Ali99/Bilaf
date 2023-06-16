from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request: HttpRequest):
    if request.method == "POST":
        print("post")
        try:
            user = User.objects.create_user(
                username=request.POST["user_name"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                password=request.POST["password"],
            )
            user.save()
            return redirect("main_app:home_page")
        except:
            print("error")
            msg = "Username taken!"
    return render(request, "users_app/login.html")


def login_page(request: HttpRequest):
    if request.user.is_authenticated:
        print(request.user.username)
        return redirect("main_app:home_page")
    #if user login already redirect to home page

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
