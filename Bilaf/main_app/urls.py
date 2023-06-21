from . import views
from django.urls import path


app_name = "main_app"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("base/", views.base_page, name="base"),
    path("cart/", views.shoping_cart, name="cart"),
    path("view_order/<int:cart_id>/", views.view_order, name="view_order"),
    path("check_out/", views.check_out, name="check_out"),
    path("about_us/", views.about_us, name="about_us"),
    path("about_bilaf/", views.about_project, name="about_bilaf"),
    path("policies/", views.pick_delv_policies, name="policies"),
    path("searched/", views.search_the_store, name="search"),
    path("merchant/adding_products/", views.merchant_adding_products, name="merchant_adding_product"),
    path("merchant/adding_categories/", views.merchant_adding_categories, name="merchant_adding_categories"),
    path("product/", views.product_page, name="product_page"),
    path("detail/<product_id>/", views.product_detail, name="product_detail"),
    path("product/update/<product_id>/", views.update_product, name="update_product"),
    path("product/delete/<product_id>/", views.delete_product, name="delete_product"),
    path("product/detail/<product_id>/", views.product_detail, name="product_detail"),
    path("catgory/", views.catgory_page, name="catgory_page"),
    path(
        "catgory/update/<categories_id>/", views.update_catgory, name="update_catgory"
    ),
    path(
        "catgory/delete/<categories_id>/", views.delete_product, name="delete_catgory"
    ),
    path("stores/", views.merchants_store_pages, name="merchants_store_pages"),
    path("merchant/dashboard/", views.dashboard_view, name="merchant_dashboard"),
    path("orders/", views.orders, name="orders_status"),
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path('thanks_page/', views.thanks_order_page, name="thanks_order_page"),
    path("cart/place_order/", views.place_order, name="place_order"),
    path("cart/update_cart/", views.update_cart, name="update_cart"),
    path(
        "cart/delete_cart_item/<int:cart_item>",
        views.delete_cart_item,
        name="delete_cart_item",
    ),
    path("orders/<action>/<cart_id>", views.order_action, name="order_action"),
    path("customer/<store_id>/products", views.customer_viewing_products, name="customer_viewing_products"),
    
    path("user/<product_id>/products", views.unregistered_customer_product_detail, name="unregistered_customer_product_detail"),
]
