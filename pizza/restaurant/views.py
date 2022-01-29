from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .serializers import *


def homepage(requests):
    return HttpResponse("<p>Test task. REST API. @Biometric / Shukurov Almaz<p>")


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PizzaSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RestaurantSerializer
