from django.urls import path

from .views import create_product, get_products, index

urlpatterns = [
    path('', index, name='index'),
    path('products/', get_products, name='get_products'),
    path('products/create/', create_product, name='create_product'),
]
