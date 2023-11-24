from django.urls import path
from .views import *


urlpatterns = [
    path('',HomeTemplateView.as_view() , name='home'),
    path('shop', shop_grid, name='shop_grid'),
    path('shop_details', shop_details, name='shop_details'),
    path('shopping_cart', ShoppingCartTemplateView.as_view(), name='shopping_cart'),
    path('checkout', checkout, name='checkout'),
    path('blog_details', blog_details, name='blog_details'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),
]
