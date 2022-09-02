from django.db import models

from django.db import models


class RestaurantChain(models.Model):
    name = models.CharField(max_length=50)
    parent_company = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.parent_company}'


class Place(models.Model):
    chain = models.ForeignKey(RestaurantChain, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name
