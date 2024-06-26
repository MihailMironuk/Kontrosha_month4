from django.db import models


class Slogan(models.Model):
    text = models.CharField(max_length=255)


class YouTubeVideo(models.Model):
    url = models.URLField()


class TopProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    popularity = models.IntegerField()

    def __str__(self):
        return self.name
