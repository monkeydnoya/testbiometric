from django.urls import path
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('api/pizza', PizzaViewSet, 'pizza')
router.register('api/restaurant', RestaurantViewSet, 'restaurant')

urlpatterns = [
    path('', homepage)
]

urlpatterns += router.urls
