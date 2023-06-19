from django.contrib import admin
from .models import Profile, Store

# # Register your models here.


class Profile_Admin(admin.ModelAdmin):
    list_display = ("id", "user", "phone_number")


class Store_Admin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "store_name",
        "category",
        "logo",
        "about",
        "pick_up_enabled",
        "delivery_enabled",
        "twitter_link",
        "instagram_link",
        "snapchat_link",
    )


admin.site.register(Store, Store_Admin)
admin.site.register(Profile, Profile_Admin)
