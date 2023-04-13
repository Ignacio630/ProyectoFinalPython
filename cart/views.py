from django.shortcuts import render
from django.shortcuts import redirect
from products.models import Products
from .models import Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def cart_product(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = 0
    for item in cart_items:
        total += item.total_price
        
    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'cart/cart_products.html', context=context)


@login_required(login_url='login_form')
def add_product(request, product_id):
    product = Products.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(user=request.user, product=product)
        cart.quantity += 1
        cart.total_price = cart.quantity * product.price
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user, product=product, quantity=1, total_price=product.price)
    cart.save()
    return redirect('cart_products')

def delete_product(request, product_id):
    if request.method == 'POST':
        product = Products.objects.get(id=product_id)
        cart = Cart.objects.get(product=product, user=request.user)
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.total_price = cart.quantity * product.price
            cart.save()
        else:
            cart.delete()
        return redirect('cart_products')