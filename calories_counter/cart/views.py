from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.decorators.http import require_POST
from cart.cart import Cart
from .forms import CartEditProductQuantityForm, CalcForm
from main_app.models import Product
from .calculator import calculator


# Create your views here.
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    print('product got')
    form = CartEditProductQuantityForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    form = CartEditProductQuantityForm(request.POST)
    product = get_object_or_404(Product, id=product_id)
    if form.is_valid():
        cd = form.cleaned_data
        cart.remove(product=product,
                    quantity=cd['quantity'],
                    update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    form = CartEditProductQuantityForm()
    calc_form = CalcForm()
    return render(request, 'cart/cart_detail.html',
                  {'cart': cart, 'form': form, 'calc_form': calc_form})


def cart_calculator(request):
    if request.method == 'POST':
        calc_form = CalcForm(request.POST)
        if calc_form.is_valid():
            cleaned_data = calc_form.cleaned_data
            physical_activity_choice = cleaned_data['physical_activity']
            weight = cleaned_data['weight']
            height = cleaned_data['height']
            age = cleaned_data['age']
            gender = cleaned_data['gender']
            result = calculator(gender, weight, height, age, physical_activity_choice)
            request.session['result'] = result
            return redirect('cart:cart_detail')
