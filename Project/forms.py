
from django import forms
from .models import Restaurant, MenuItem, Order

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'phone_number']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['restaurant', 'name', 'description', 'price']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['menu_item', 'quantity']
