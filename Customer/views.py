from django.shortcuts import render


def CustomerHomePage(request):
    return render(request, 'Customer/CustomerHomePage.html')

def CustomerListPizza(request):
    return render(request, 'Customer/CustomerListPizza.html')
def CustomerListBrownie(request):
    return render(request, 'Customer/CustomerListBrownie.html')

def TrackOrder(request):
    return render(request, 'Customer/TrackOrder.html')


from django.shortcuts import render
from django.shortcuts import render, redirect
from Project.forms import RestaurantForm, MenuItemForm, OrderForm

# Create your views here.
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Customer:order_list')
    else:
        form = OrderForm()
    return render(request, 'Customer/add_order.html', {'form': form})





from django.shortcuts import render
from .models import Restaurant, MenuItem, Order

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'Customer/restaurant_list.html', {'restaurants': restaurants})

def menu_item_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'Customer/menu_item_list.html', {'menu_items': menu_items})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'Customer/order_list.html', {'orders': orders})


from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Customer/confirmation.html')
    else:
        form = FeedbackForm()
    return render(request, 'Customer/feedbackform.html', {'form': form})
