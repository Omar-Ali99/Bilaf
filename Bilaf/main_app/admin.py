from django.contrib import admin
from .models import Product,Categories

# Register your models here.



class Product_Admin(admin.ModelAdmin):
    list_display = ("store", "name","category","price","quantity","is_active","description","image")

admin.site.register(Product, Product_Admin)

class Categories_Admin(admin.ModelAdmin):
    list_display = ("store", "name","logo")

admin.site.register(Categories, Categories_Admin)