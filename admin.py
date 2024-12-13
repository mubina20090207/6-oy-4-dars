from django.contrib import admin
from .models import Brand, Car

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'established')
    search_fields = ('name', 'country')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'year', 'price')
    list_filter = ('brand', 'year')
    search_fields = ('name',)
