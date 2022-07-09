
from django.urls import path
from .views import *
from rest_producto.views import variosProductos,detalle_producto


urlpatterns = [
    path('productos', variosProductos),
    path('detalle_producto', detalle_producto),

]
