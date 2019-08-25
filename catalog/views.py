from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .client import ProductClient


class Product(APIView):
    def get(self, request):
        return Response({'product': ProductClient(1).get_data()})


class Products(APIView):
    def get(self, request):
        products = map(lambda id: ProductClient(id).get_data(), range(0, 5))
        products = filter(None, products)
        return Response({'products': list(products)})
