from django.contrib import admin
from .models import *

# Register your models here.


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cheese', 'thickness', 'secret', 'restaurant')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'restaurant')


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
