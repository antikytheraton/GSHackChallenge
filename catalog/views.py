from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .client import ProductClient
from .documents import ProductDocument


class Favorites(APIView):
    def post(self, request):
        # id = request.data.get('id')
        # products = ProductDocument.objects(prod_id=id)
        # products.delete()
        queryset = ProductDocument(request.data)
        queryset.save()
        return Response(queryset.to_json())

    def get(self, request):
        queryset = ProductDocument.objects
        return Response(list(queryset))



class Products(APIView):
    def get(self, request):
        products = map(lambda id: ProductClient(id).get_data(), range(0, 2))
        products = filter(None, products)
        return Response({'products': list(products)})
