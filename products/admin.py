from django.contrib import admin
from .models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'slug')
    list_display_links = ('__unicode__', 'slug')
    class Meta:
        model = Products

admin.site.register(Products, ProductsAdmin)