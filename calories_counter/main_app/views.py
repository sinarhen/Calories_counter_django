from django.shortcuts import render
from .models import *


# Create
# your views here.


def index(request):
    """Index welcome page"""
    return render(request, template_name="main_app/index.html")


def catalog(request):
    """Catalog is where all products located"""
    categories = FoodType.objects.all()
    products = FoodType.objects.all()
    return render(request, template_name="main_app/catalog.html")
