from . import views
from django.urls import path

app_name = "main_app"

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('base/', views.base_page , name = 'base'),
    path('add/', views.add_page , name = 'add_page')

   
]