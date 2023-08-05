from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

# Namespace for the cart app
app_name = 'cart'

# URL patterns for the cart app
urlpatterns = [
    # Cart detail view
    path('', cart_detail, name='cart_detail'),
    
    # Cart add view
    path('add/<int:product_id>', cart_add, name='cart_add'),
    
    # Cart remove view
    path('remove/<int:product_id>', cart_remove, name='cart_remove'),
    
    # Cart calculator view
    path('calculator', cart_calculator, name='calculator'),
]
