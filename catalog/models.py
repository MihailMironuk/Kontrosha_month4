from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    popularity = models.IntegerField()

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Review by {self.author} for {self.product.name}"
