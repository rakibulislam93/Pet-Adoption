from django.db import models
from django.contrib.auth.models import User
from .constrant import RATINGS
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class Pet(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='pets')
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=12,decimal_places=2)
    age = models.IntegerField()
    image = models.ImageField(upload_to="pet/images/")
    available = models.BooleanField(default=True)
    added_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='add_pets')

    def __str__(self) -> str:
        return self.name


class Adoption(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='adoptions')
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE,related_name='adoptions')
    adoption_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} adopted {self.pet.name}"


class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE,related_name='reviews')
    rating = models.CharField(choices=RATINGS,max_length=20)
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)