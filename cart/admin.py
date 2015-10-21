from django.contrib import admin
from .models import Cart

# admin settings for any products
class CartAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'user')
    list_display_links = ('__unicode__', 'user')
    class Meta:
        model = Cart

admin.site.register(Cart, CartAdmin)