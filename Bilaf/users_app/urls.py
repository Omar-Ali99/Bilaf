from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path('sign_up/', views.signup_page, name = 'signup_page'),

    path('login/', views.login_page, name = 'login_page'),

    path('signout/', views.signout_page, name = 'signout_page'),

    path('no_permission_page/', views.no_permission_page, name = 'no_permission_page')
]