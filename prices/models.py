from django.db import models


class ProductPrice(models.Model):
    name = models.CharField(max_length=255)  # Nazwa produktu
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Cena produktu, do 2 miejsc po przecinku
    store_name = models.CharField(max_length=255)  # Nazwa sklepu
    product_url = models.URLField()  # URL produktu w sklepie
    date_collected = models.DateField()  # Data zebrania ceny

    def __str__(self):
        return f"{self.name} - {self.price} ({self.store_name})"