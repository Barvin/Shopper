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
        cart = request.session['cart']
        # match Cart id with session
        update_cart = Cart.objects.get(id=cart)
        update_cart.products.add(product)
        update_cart.save()
        request.session['total_items'] = len(update_cart.products.all())
    except KeyError:
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
        cart_loopkup = Cart.objects.get(id=cartID)
    except KeyError:
        cart_loopkup = False
    return render_to_response('cart/cart.html', locals(), context_instance=RequestContext(request))