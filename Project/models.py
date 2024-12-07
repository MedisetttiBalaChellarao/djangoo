from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name



from django.db import models
# Adjust the import as necessary

class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='project_orders')
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.menu_item



