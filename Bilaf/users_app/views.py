from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup_page(request: HttpRequest):
    msg = None
    if request.method == "POST":
        try:
            user = User.objects.create_user(
                username = request.POST["username"],
                first_name = request.POST["first_name"],
                last_name = request.POST["last_name"],
                email = request.POST["email"],
                password = request.POST["password"]
            )
            user.save()

            return redirect("users_app:login_page")
        except:
            msg = "Username taken!"

    return render(request, 'users_app/sign_up.html', {"msg" : msg})


def login_page(request: HttpRequest):
    msg = None
    if request.method == "POST":
        user : User = authenticate(request, username = request.POST["username"], password = request.POST["password"])
        if user:
            login(request, user)
            return redirect("main_app:home+page")
        else:
            msg = "Incorrect Credentials"

    return render(request, 'users_app/login.html', {"msg" : msg})


def signout_page(request: HttpRequest):
    logout(request)

    return redirect('main_app:home_page')


def no_permission_page(request: HttpRequest):
    return render(request, "users_app/no_permission.html")