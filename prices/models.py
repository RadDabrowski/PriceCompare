from django.db import models


class ProductPrice(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store_name = models.CharField(max_length=255)
    product_url = models.URLField()
    date_collected = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.price} ({self.store_name})"
