from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('products', products, name='products'),
    path('search', search_view, name='search_view'),
]
