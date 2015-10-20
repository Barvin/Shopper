from datetime import date
from django.http import HttpResponse
from django.template import RequestContext
from .models import Products
from django.shortcuts import render_to_response

# Create your views here.
def product_page(request):
    results = Products.objects.all()
    
    return render_to_response("results.html", locals(), context_instance=RequestContext(request))

def product_single(request, slug):    
    product = Products.objects.get(slug=slug)
    
    return render_to_response("product.html", locals(), context_instance=RequestContext(request))