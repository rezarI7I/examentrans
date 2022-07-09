from django.forms import ModelForm
from .models import *
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo','nombre','precio','foto']
class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo','categoria']

