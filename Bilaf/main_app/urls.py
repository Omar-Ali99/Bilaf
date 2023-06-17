from . import views
from django.urls import path

app_name = "main_app"

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('base/', views.base_page , name = 'base'),
    path('add/', views.add_page , name = 'add_page'),
    path('detail/', views.product_details , name = 'product_details'),
    path('cart/', views.shoping_cart , name = 'shoping_cart'),
    path('check_out/', views.check_out , name = 'check_out'),
    path('contact/', views.contect_us , name = 'contact_us'),

]