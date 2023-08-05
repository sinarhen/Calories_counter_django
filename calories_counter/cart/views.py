from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.decorators.http import require_POST
from cart.cart import Cart
from .forms import CartEditProductQuantityForm, CalcForm
from main_app.models import Product
from .calculator import calculator


# Add product to cart
@require_POST
def cart_add(request, product_id):
    """
    Adds a product to the cart with the specified quantity.
    
    Arguments:
    - request: The HTTP request object.
    - product_id: The ID of the product to be added to the cart.
    
    Returns:
    - A redirect to the cart detail page.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartEditProductQuantityForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


# Remove product from cart
@require_POST
def cart_remove(request, product_id):
    """
    Removes a product from the cart with the specified quantity.
    
    Arguments:
    - request: The HTTP request object.
    - product_id: The ID of the product to be removed from the cart.
    
    Returns:
    - A redirect to the cart detail page.
    """
    cart = Cart(request)
    form = CartEditProductQuantityForm(request.POST)
    product = get_object_or_404(Product, id=product_id)
    if form.is_valid():
        cd = form.cleaned_data
        cart.remove(product=product,
                    quantity=cd['quantity'],
                    update_quantity=cd['update'])
    return redirect('cart:cart_detail')


# Display cart details
def cart_detail(request):
    """
    Displays the contents of the cart.
    
    Arguments:
    - request: The HTTP request object.
    
    Returns:
    - The rendered cart detail page.
    """
    cart = Cart(request)
    form = CartEditProductQuantityForm()
    calc_form = CalcForm()
    return render(request, 'cart/cart_detail.html',
                  {'cart': cart, 'form': form, 'calc_form': calc_form})


# Perform calculations for cart
def cart_calculator(request):
    """
    Performs calculations based on user input and stores the result in the session.
    
    Arguments:
    - request: The HTTP request object.
    
    Returns:
    - A redirect to the cart detail page.
    """
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
