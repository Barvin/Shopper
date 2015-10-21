from django.contrib import admin
from .models import Contact

# admin settings for any products
class ContactAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'message', 'timestamp')
    list_display_links = ('__unicode__', 'timestamp')
    class Meta:
        model = Contact

admin.site.register(Contact, ContactAdmin)

