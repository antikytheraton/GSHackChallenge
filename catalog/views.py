from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .client import ProductClient
from .documents import ProductDocument


class Favorites(APIView):
    def post(self, request):
        id = request.data.get('id')
        prods = ProductDocument.objects(prod_id=id)
        prods.delete()
        queryset = ProductDocument(**request.data)
        queryset.save()
        return Response(queryset.to_json())

    def get(self, request):
        queryset = ProductDocument.objects
        queryset = list(map(lambda qs: qs.to_json(), queryset))
        return Response(list(queryset))


class Products(APIView):
    def get(self, request):
        products = map(lambda id: ProductClient(id).get_data(), range(0, 2))
        products = filter(None, products)
        return Response({'products': list(products)})


class Auctions(APIView):
    def post(self, request, id):
        queryset = ProductDocument.objects(prod_id=int(id)).first()
        offer = request.data.get('offer', None)
        if offer:
            queryset.save()
            queryset.update(inc__offers=[offer, ])
        return Response(queryset.to_json())
