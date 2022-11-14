from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import *
from api.models import *

class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    authentication_classes = []
    queryset = Dog.objects.all()
    serializer = DogSerializer


class BreedViewSet(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    authentication_classes = []
    queryset = Breed.objects.all()
    serializer = BreedSerializer

###
#class DogViewSet(viewsets.ModelViewSet):
#    authentication_classes = []
#    queryset = Dog.objects.all()
#    serializer_class = DogSerializer
#
#class BreedViewSet(viewsets.ModelViewSet):
#    authentication_classes = []
#    queryset = Breed.objects.all()
#    serializer_class = BreedSerializer
