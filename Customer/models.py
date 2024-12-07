from django.db import models
from django.contrib.auth.models import User


from django.shortcuts import render, redirect
from Project.models import Restaurant, MenuItem, Order  # Ensure all models are imported
from Project.forms import RestaurantForm, MenuItemForm, OrderForm

from django.db import models
  # Adjust the import as necessary


from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)  # Added phone number field
    comments = models.TextField(max_length=150)

    def __str__(self):
        return self.name
