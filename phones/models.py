from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(max_length=350)
    release_date = models.DateTimeField(max_length=20)
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)


