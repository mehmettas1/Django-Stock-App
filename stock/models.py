from secrets import choice
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Firm(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name="product_category", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name="product_brand", on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANS = (
        ("in", "IN"),
        ("out", "OUT"),
    )
    user = models.ForeignKey(User, related_name="transaction_owner", on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, related_name="transaction_firm", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="transaction_product", on_delete=models.CASCADE)
    transaction = models.CharField(max_length=50, choices=TRANS)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    price_total = models.DecimalField(max_digits=20, decimal_places=2, blank=True)


    # def __str__(self):
    #     return f'{self.user} - {self.product} - {self.transaction}'

    # def price_total_calc(self):
    #     self.price_total = self.price * self.quantity
    #     return self.price_total