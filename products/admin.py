from django.contrib import admin
from .models import Products

# admin settings for any products
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'slug')
    list_display_links = ('__unicode__', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    class Meta:
        model = Products

admin.site.register(Products, ProductsAdmin)