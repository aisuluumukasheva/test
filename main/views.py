from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from .models import Product


@api_view(['GET'])
def test(request):
    return Response({'message': 'hello world'}, 200)

@api_view(['GET'])
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset,many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def product_details(request, id):
    # product = Product.objects.get(id=id) - выйдет ошибка, если такого id не существует
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=200)
    