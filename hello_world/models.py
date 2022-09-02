from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
