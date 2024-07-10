from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta : 
        model = models.Category
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):
    class Meta : 
        model = models.Pet
        fields = '__all__'


class AdoptionSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Adoption
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Review
        fields = '__all__'
        