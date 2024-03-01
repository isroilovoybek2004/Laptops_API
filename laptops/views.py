from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from laptops.models import Laptops
from laptops.serializers import LaptopsSerializer


class LaptopsAPIView(APIView):
    def get(self, request):
        laptops = Laptops.objects.all()
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(laptops, request)
        serializer = LaptopsSerializer(page_obj, many=True)
        return paginator.get_paginated_response(data=serializer.data)

    def delete(self, request, pk):
        laptops = Laptops.objects.get(pk=pk)
        laptops.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        laptops = Laptops.objects.get(pk=pk)
        serializer = LaptopsSerializer(instance=laptops, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        laptop = Laptops.objects.get(pk=pk)
        serializer = LaptopsSerializer(laptop, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
