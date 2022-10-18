from django.shortcuts import render, redirect
from .models import *
from cart.forms import CartEditProductQuantityForm
from cart.views import *


# Create
# your views here.


def index(request):
    """Index welcome page"""
    return render(request, template_name="main_app/index.html")


def catalog(request):
    """Catalog is where all products located"""
    categories = FoodType.objects.all()
    products = Product.objects.all()
    return render(request, template_name="main_app/catalog.html", context={'categories': categories,
                                                                           'products': products})


def detail_view_category(request, category_pk):
    products = Product.objects.filter(type_of_food_id=category_pk)
    return render(request, template_name="main_app/detail_category.html",
                  context={'products': products, 'name': FoodType.objects.get(id=category_pk)})


def detail_view_product(request, category_pk, product_pk):
    product = Product.objects.get(id=product_pk)
    form = CartEditProductQuantityForm()
    return render(request, template_name='main_app/detail_product.html', context={'product': product, 'form': form})
