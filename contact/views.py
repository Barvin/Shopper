from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from .form import ContactForm


# Create your views here.

def contactForm(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        validForm = form.save(commit=False)
        validForm.save()
        return HttpResponseRedirect('/static/templates/redirect.html')
    
    return render_to_response("contact/form.html", locals(), context_instance=RequestContext(request))