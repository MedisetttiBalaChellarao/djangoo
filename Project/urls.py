from django.urls import path, include
from. import views

urlpatterns = [
    path('', views.projecthomepage, name= 'projecthomepage'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserLoginPageCall', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic', views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/',views.logout,name='logout'),
    path('payment/', views.payment, name='payment'),


]