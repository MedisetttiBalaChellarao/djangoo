from django.urls import path, include
from . import views
app_name = 'Customer'

urlpatterns = [
    path('CustomerHomePage/',views.CustomerHomePage,name="CustomerHomePage"),
    path('CustomerListPizza/',views.CustomerListPizza,name="CustomerListPizza"),
    path('CustomerListBrownie/',views.CustomerListBrownie,name="CustomerListBrownie"),
    path('TrackOrder/', views.TrackOrder, name="TrackOrder"),

    path('add_order/',views.add_order,name="add_order"),
    path('feedback/', views.feedback_view, name='feedback'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),  # Ensure this line is present
    path('menu-items/', views.menu_item_list, name='menu_item_list'),  # Ensure this line is present
    path('orders/', views.order_list, name='order_list'),

]
