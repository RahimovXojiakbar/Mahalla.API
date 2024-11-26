from rest_framework.serializers import ModelSerializer, SlugRelatedField
from . models import Neighborhood, House

class NeighborhoodSerializer(ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = '__all__'

class HouseSerializer(ModelSerializer):
    neighborhood = SlugRelatedField(slug_field = 'title', read_only=True)
    class Meta:
        model = House
        fields = '__all__'
