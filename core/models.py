from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order {self.id}"
