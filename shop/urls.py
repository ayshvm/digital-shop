
from django.contrib import admin
from django.urls import path
from shop.views import index, login, productDetails

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('product/<int:product_id>', productDetails, name='details'),
]
