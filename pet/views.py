from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetSerializer


class AdoptionViewSet(viewsets.ModelViewSet):
    queryset = models.Adoption.objects.all()
    serializer_class = serializers.AdoptionSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    

