from django.contrib import admin
from .models import merchant_profile, customer_profile

# Register your models here.

class Merchant_Profile_Admin(admin.ModelAdmin):
    list_display = (
        "user",
        "merchant_name",
    )


admin.site.register(merchant_profile,Merchant_Profile_Admin)