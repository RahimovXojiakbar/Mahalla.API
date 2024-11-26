from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import NeighborhoodSerializer, HouseSerializer
from . models import Neighborhood, House
from rest_framework.response import Response

class NeighborhoodView(APIView):
    def get(self, request, format=None):
        neighborhoods = Neighborhood.objects.all()
        serializer = NeighborhoodSerializer(neighborhoods, many=True)
        return Response(serializer.data)
    

class HouseView(APIView):
    def get(self, request, format=None):
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many = True)
        return Response(serializer.data)
    
