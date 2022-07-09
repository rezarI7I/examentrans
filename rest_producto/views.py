from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from sqlalchemy import true
from core.models import Producto, Producto, Vehiculo
from rest_producto.serializers import ProductoSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
@api_view(['GET','POST'])
def variosProductos(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['PUT','DELETE'])
def detalle_producto(request, id):
    try:
        producto = Producto.objects.get(patente=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Vehiculo.delete()
        return Response(status.HTTP_204_NO_CONTENT)