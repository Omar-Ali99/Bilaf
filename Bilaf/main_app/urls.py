from . import views
from django.urls import path

app_name = "main_app"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("base/", views.base_page, name="base"),
    path("add/", views.add_page, name="add_page"),
    path("cart/", views.shoping_cart, name="cart"),
    path("check_out/", views.check_out, name="check_out"),
    path("about_us/", views.about_us, name="about_us"),
    path("about_bilaf/", views.about_project, name="about_bilaf"),
    path("policies/", views.pick_delv_policies, name="policies"),
    path("searched/", views.search, name="search"),
    path("merchant/adding_products/", views.add_product, name="add_product"),
    path("merchant/adding_categories/", views.add_categories, name="add_categories"),
    path("product/", views.product_page, name="product_page"),
    path("detail/<product_id>/", views.product_detail, name="product_detail"),
    path("store/", views.store_page, name="store_page"),
    path("merchant/dashboard/", views.dashboard_view, name="dashboard"),
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
]
