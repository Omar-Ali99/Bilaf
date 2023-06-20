from . import views
from django.urls import path

app_name = "main_app"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("base/", views.base_page, name="base"),
    path("cart/", views.shoping_cart, name="cart"),
    path("view_order/", views.view_order, name="view_order"),
    path("check_out/", views.check_out, name="check_out"),
    path("about_us/", views.about_us, name="about_us"),
    path("about_bilaf/", views.about_bilaf, name="about_bilaf"),
    path("policies/", views.pick_delv_policies, name="policies"),
    path("searched/", views.search, name="search"),
    path("merchant/adding_products/", views.merchant_adding_products, name="merchant_add_product"),
    path("merchant/adding_categories/", views.merchant_adding_categories, name="merchant_add_categories"),
    path("product/", views.product_page, name="product_page"),
    path('detail/<product_id>/', views.product_detail , name = 'product_detail'),
    path("merchant/product/update/<product_id>/", views.merchant_update_product, name="merchant_update_product"),
    path("merchant/product/delete/<product_id>/", views.merchant_delete_product, name="merchant_delete_product"),
    path('product/detail/<product_id>/', views.product_detail , name = 'product_detail'),
    path("merchant/category/update/<categories_id>/", views.merchant_update_category, name="merchant_update_catgory"),
    path("merchant/category/delete/<categories_id>/", views.merchant_delete_category, name="merhcant_delete_catgory"),
    path("stores/", views.all_stores_pages, name="store_pages"),
    path('merchant/dashboard/', views.merchant_dashboard_view, name='merchant_dashboard'),
    path("order_status/", views.order_status, name="order_status"),
    path('add_to_cart', views.add_to_cart, name="add_to_cart")


]
