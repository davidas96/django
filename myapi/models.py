from django.db import models

# Create your models here.


class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name
