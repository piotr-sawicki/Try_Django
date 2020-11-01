from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title =       models.CharField(max_length=120) # max_length is required
    description = models.TextField(blank=True, null=True)
    price =       models.DecimalField(decimal_places=2, max_digits=10000)
    feature =   models.BooleanField(default=False)
    summary =     models.TextField()

    def get_absolute_url(self):
        # return f'/product/{self.id}/'
        return reverse('products:product-detail', kwargs={"id": self.id})
