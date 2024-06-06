from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class FoodType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    composition = models.TextField()
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text