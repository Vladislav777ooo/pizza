from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<product_id>', views.cart_add, name='cart_add'),
    path('remove/P<product_id>', views.cart_remove, name='cart_remove'),
]