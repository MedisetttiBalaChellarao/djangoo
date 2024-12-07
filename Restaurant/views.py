from django.shortcuts import render

# Create your views here.
def RestaurantHomePage(request):
    return render(request, 'Restaurant/RestaurantHomePage.html')


from django.shortcuts import render
from django.shortcuts import render, redirect
from Project.forms import RestaurantForm, MenuItemForm, OrderForm
def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Restaurant:menu_item_list')
    else:
        form = MenuItemForm()
    return render(request, 'Restaurant/add_menu_item1.html', {'form': form})

def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Restaurant:restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'Restaurant/add_restaurant1.html', {'form': form})

from django.shortcuts import render
from .models import Restaurant, MenuItem,Order

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'Restaurant/restaurant_list1.html', {'restaurants': restaurants})

def menu_item_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'Restaurant/menu_item_list1.html', {'menu_items': menu_items})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'Restaurant/order_list1.html', {'orders': orders})