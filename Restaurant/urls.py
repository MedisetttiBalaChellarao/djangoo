from django.urls import path, include
from . import views
app_name = 'Restaurant'

urlpatterns = [
    path('RestaurantHomePage/',views.RestaurantHomePage,name="RestaurantHomePage"),
    path('add_menu_item/', views.add_menu_item, name="add_menu_item"),
    path('add_restaurant/', views.add_restaurant, name="add_restaurant"),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),  # Ensure this line is present
    path('menu-items/', views.menu_item_list, name='menu_item_list'),  # Ensure this line is present
    path('orders/', views.order_list, name='order_list'),

]
