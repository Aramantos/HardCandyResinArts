from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_products, name='shop_products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]