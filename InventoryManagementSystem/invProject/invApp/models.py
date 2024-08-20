from django.db import models


# Create your models here.
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=20, decimal_places=2)
    product_quantity = models.IntegerField()
    product_supplier = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name
