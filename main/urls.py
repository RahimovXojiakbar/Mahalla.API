from django.urls import path
from . views import NeighborhoodView, HouseView

urlpatterns = [
    path('neighborhoods/', NeighborhoodView.as_view(), name='neighborhood_url'),
    path('houses/', HouseView.as_view(), name='house_url'),
    
]