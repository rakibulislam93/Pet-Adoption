from django.contrib import admin
from . import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('name',)}


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Pet)
admin.site.register(models.Adoption)
admin.site.register(models.Review)