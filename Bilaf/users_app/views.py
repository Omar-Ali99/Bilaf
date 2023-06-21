from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Store
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
            group = Group.objects.get(name="customers")
            request.user.groups.add(group)
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


@login_required(login_url="/users/login/")
def became_marchant(request: HttpRequest):
    # checkboxes = {
    #     "pick_up_enabled": False,
    #     "delivery_enabled": False,
    # }
    if request.method == "POST":
        # available_checkboxes = {key: key in request.POST for key in checkboxes.keys()}

        if "pick_up_enabled" in request.POST:
            pick_up = True
        else:
            pick_up = False
        if "delivery_enabled" in request.POST:
            delivery = True
        else:
            delivery = False
        if "logo" in request.FILES:
            new_logo = request.FILES["logo"]
        new_marchant = Store(
            owner=request.user,
            store_name=request.POST["store_name"],
            about=request.POST["about"],
            category="Saudi-Arabian",
            logo=new_logo,
            pick_up_enabled=pick_up,
            delivery_enabled=delivery,
        )
        try:
            new_marchant.save()
        except Exception as e:
            print(e)
        group = Group.objects.get(name="merchant")
        request.user.groups.add(group)
        return redirect("main_app:home_page")

    return render(request, "users_app/became_merchant.html")


