from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=128, unique=True)
    product_description = models.CharField(max_length=512, unique=True)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_stock = models.IntegerField(blank=True, null=True)
    product_image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_id = models.CharField(max_length=128, unique=True)
    order_qty = models.IntegerField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    product_stock = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.order_id
    