from django.db import models


# Create your models here.
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, allow_unicode=True)
    excerpt = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    stock = models.PositiveIntegerField(default=1)
    stock_limit = models.PositiveIntegerField(default=5)
    price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    sale_start_date = models.DateTimeField(null=True, blank=True)
    sale_end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductImage(models.Model):
    src = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return str(self.src)
