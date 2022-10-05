from django.shortcuts import render
from .models import *


# Create
# your views here.


def index(request):
    """Index welcome page"""
    return render(request, template_name="main_app/index.html")


def calculator(request):
    """Catalog is where all products located"""
    categories = FoodType.objects.all()
    products = Product.objects.all()
    return render(request, template_name="main_app/catalog.html", context={'categories': categories,
                                                                           'products': products})
