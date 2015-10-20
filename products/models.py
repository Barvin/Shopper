from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(null=True, blank=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
    # defines the ordering of the class' data should be in reverse
    class Meta:
        ordering = ['-name']
    
