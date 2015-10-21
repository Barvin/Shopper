from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from .models import Cart
from products.models import Products
# Create your views here.

def add(request, slug):
    product = Products.objects.get(slug=slug)
    request.session.set_expiry(30)

    # start a cart if none (i.e. doesn't have a cart id)
    try:
        active = request.session['cart']
    except:
    # initialize new cart to 'Empty'
        request.session['cart'] = 'Empty'

    if request.session['cart'] is not "Empty":
        cart = request.session['cart']
        # match Cart id with session
        update_cart = Cart.objects.get(id=cart)
        update_cart.products.add(product)
        update_cart.save()
        request.session['total_items'] = len(update_cart.products.all())
    else:
        # add product to empty cart
        cart = Cart()
        cart.save()
        cart.products.add(product)
        # change 'empty' session to cart id
        request.session['cart'] = cart.id
        request.session['total_items'] = len(cart.products.all())

    return HttpResponseRedirect('/products/' + slug)
