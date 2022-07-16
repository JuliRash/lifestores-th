from django.db import models

    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description =  models.TextField()
    sku = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.URLField()
    
    def __Str__(self):
        return self.name