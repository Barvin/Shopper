from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from .models import Cart
from products.models import Products
import pdb
# Create your views here.

def add(request, slug):
    product = Products.objects.get(slug=slug)

    # session expiration(seconds = 24h)
    request.session.set_expiry(90000)

    # start a cart if none (i.e. doesn't have a cart id)
    try:
        cart = request.session['cart']
        # match Cart id with session
        update_cart = Cart.objects.get(id=cart)
        update_cart.products.add(product)
        update_cart.save()

        # create key-value pair
        request.session['total_items'] = len(update_cart.products.all())
    except:
        # initialize new cart to 'Empty'
        request.session['cart'] = 'Empty'
        # add product to empty cart
        new_cart = Cart()
        new_cart.save()
        new_cart.products.add(product)
        # change 'empty' session to cart id
        request.session['cart'] = new_cart.id
        request.session['total_items'] = len(new_cart.products.all())

    return HttpResponseRedirect('/products/' + slug)

def view(request):
    try:
        cartID = request.session['cart']
        getCart = Cart.objects.get(id=cartID)
    except:
        getCart = False
        try:
            request.session['total_items'] == 0
        except:
            pass

    if getCart == False or getCart.active == False:
        poi = "Your cart is empty."
    if getCart and getCart.active:
        cart = getCart
    return render_to_response('cart/cart.html', locals(), context_instance=RequestContext(request))

def delete(request):
    try:
        cartID = request.session['cart']
        cart = Cart.objects.get(id=cartID)
        cart.active = False
        cart.save()
        request.session['total_items'] = 0

        # destroy session
        request.session.flush()
    except:
        cart = False

    return HttpResponseRedirect('/cart/')