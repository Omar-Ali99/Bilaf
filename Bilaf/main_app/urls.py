from . import views
from django.urls import path

app_name = "main_app"

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('about_us/', views.about_us , name = 'about_us'),
    path('about_bilaf/', views.about_project , name = 'about_bilaf'),
    path('policies/', views.pick_delv_policies , name = 'policies'),
   
   
]