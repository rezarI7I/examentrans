
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('crearProducto', crearVehiculo, name="crearVehiculo"),
    path('modificarVehiculo/<id>', modificarVehiculo, name="modificarVehiculo"),
    path('elimirnarVehiculo/<id>', elimirnarVehiculo, name="elimirnarVehiculo"),
    path('login', LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout', LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path('registro', registro, name="registro"),
    path('casa', casa, name="casa"),
    path('crearProductos', crearProductos, name="crearProductos"),
    path('modificarProducto/<id>', modificarProducto, name="modificarProducto"),
    path('elimirnarProducto/<id>', elimirnarProducto, name="elimirnarProducto"),
]
