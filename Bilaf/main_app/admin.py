from django.contrib import admin
from .models import Product, Categories, Cart, CartItem

# Register your models here.


class Product_Admin(admin.ModelAdmin):
    list_display = (
        "id",
        "store",
        "name",
        "category",
        "price",
        "quantity",
        "is_active",
        "description",
        "image",
    )


class Categories_Admin(admin.ModelAdmin):
    list_display = (
        "id",
        "store",
        "name",
        "logo",
    )


class Cart_Admin(admin.ModelAdmin):
    list_display = (
        "id",
        "store",
        "customer",
        "status",
        "created_at",
        "due_date",
        "delivery_option",
        "payment_option",
    )


class Cart_Item_Admin(admin.ModelAdmin):
    list_display = ("id", "cart", "product", "quantity", "price")


admin.site.register(Product, Product_Admin)
admin.site.register(Categories, Categories_Admin)
admin.site.register(Cart, Cart_Admin)
admin.site.register(CartItem, Cart_Item_Admin)
