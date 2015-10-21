import datetime
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=300)
    message = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    
    def __unicode__(self):
        return self.email
    
    # most recent first
    class Meta:
        ordering = ['-timestamp']
    