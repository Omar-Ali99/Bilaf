from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path("sign_up/", views.signup, name="signup"),
    path("login/", views.login_page, name="login"),
    path("signout/", views.signout_page, name="signout_page"),
    path("no_permission_page/", views.no_permission_page, name="no_permission_page"),
    path("became_merchant/", views.became_marchant, name="became_merchant"),
    
]
