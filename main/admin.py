from django.contrib import admin
from unfold.admin import ModelAdmin
from . models import Neighborhood, House


@admin.register(Neighborhood)
class NeighborhoodAdmin(ModelAdmin):
    list_display = ['title', 'MFY','chairman']

@admin.register(House)
class HouseAdmin(ModelAdmin):
    list_display  = ['house_boss', 'house_number', 'a_b', 'neighborhood']