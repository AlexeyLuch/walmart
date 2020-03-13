from django.db import models


class Product(models.Model):
    id_product = models.CharField(max_length=30, db_index=True)
    title = models.CharField(max_length=350, unique=True, db_index=True)
    price = models.CharField(max_length=30, db_index=True)
    url = models.CharField(max_length=350, unique=True, db_index=True)
    description = models.TextField(max_length=5000,db_index=True)
    category = models.CharField(max_length=100, db_index=True)
    rating_reviews = models.CharField(default="without rating",max_length=100, db_index=True)
    in_stock = models.BooleanField(default=True)
    brand = models.CharField(default="without brand",max_length=100, db_index=True)
    amount = models.CharField(default="quantity not indicated",max_length=10, db_index=True)
    delivery_price = models.CharField(default="Free delivery",max_length=30, db_index=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    file = models.FileField(verbose_name="id_products")
    def __str__(self):
        return self.file.name

class ProductChoiseToCart(models.Model):
    how_match_products = models.IntegerField()
    id_product = models.CharField(max_length=30, db_index=True)

class contact(models.Model):
  name = models.CharField(verbose_name = "Имя", max_length=60, blank=True, default=None)
  email = models.EmailField()
  text = models.TextField(blank=True, default=None)


