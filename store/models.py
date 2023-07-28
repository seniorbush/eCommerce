from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=128, unique=True)
    product_name = models.CharField(max_length=128, unique=True)
    product_description = models.CharField(max_length=512, unique=True)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_stock = models.IntegerField()
    # product_image = models.ImageField()