#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import *
from django.contrib.auth import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
#from django.shortcuts import render_to_response
from django.template import RequestContext


from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
from api.models import *

#REST API
from rest_framework import viewsets, filters, parsers, renderers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *

#filters
#from filters.mixins import *

from api.pagination import *
import json, datetime, pytz
from django.core import serializers
import requests


def home(request):
   """
   Send requests to / to the ember.js clientside app
   """
   return render(render, 'index.html')

class BreedsList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, format = None):
        breeds = Breed.objects.all()
        json_data = serializers.serialize('json', breeds)
        return HttpResponse(json_data, content_type='json')

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        size = request.data.get('size').upper() # Accepts Tiny, Small, Medium, Large
        friendliness = int(request.data.get('friendliness')) # Accepts ints 1-5
        trainability = int(request.data.get('trainability')) # Accepts ints 1-5
        sheddingamount = int(request.data.get('sheddingamount')) # Accepts ints 1-5
        exerciseneeds = int(request.data.get('exerciseneeds')) # Accepts ints 1-5

        newBreed = Breed(
            name = name,
            size = size,
            friendliness = friendliness,
            trainability = trainability,
            sheddingamount = sheddingamount,
            exerciseneeds = exerciseneeds
        )

        #Check that the event is safe for storage in the DB
        try:
            newBreed.clean_fields()
        except Exception as e:
            print (e)
            return Response({'success':False, 'error':e}, status=status.HTTP_400_BAD_REQUEST)

        #Log event to DB
        newBreed.save()
        return Response({'success': True}, status=status.HTTP_200_OK)


class BreedDetails(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, pk, *args, **kwargs):
        breed = Breed.objects.filter(pk = pk)
        json_data = serializers.serialize('json', breed)
        return HttpResponse(json_data, content_type = 'json')

    def put(self, request, pk, *args, **kwargs):
        breed = Breed.objects.get(pk = pk)

        if (request.data.get('name')):
            breed.name = request.data.get('name')
        if (request.data.get('size')):
            breed.size = request.data.get('size').upper()
        if (request.data.get('friendliness')):
            breed.friendliness = int(request.data.get('friendliness'))
        if (request.data.get('trainability')):
            breed.trainability = int(request.data.get('trainability'))
        if (request.data.get('sheddingamount')):
            breed.sheddingamount = int(request.data.get('sheddingamount'))
        if (request.data.get('exerciseneeds')):
            breed.exerciseneeds = int(request.data.get('exerciseneeds'))

        try:
            breed.clean_fields()
        except Exception as e:
            print (e)
            return Response({'success':False, 'error':e}, status = status.HTTP_400_BAD_REQUEST)

        #Log event to DB
        breed.save()
        return Response({'success': True}, status = status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        if (Breed.objects.filter(pk = pk).exists()):
            Breed.objects.get(pk = pk).delete()
            return Response({'success': True}, status = status.HTTP_204_NO_CONTENT)

class DogList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, format = None):
        dogs = Dog.objects.all()
        json_data = serializers.serialize('json', dogs)
        return HttpResponse(json_data, content_type = 'json')

    def post(self, request):
        name = request.data.get('name')
        age = int(request.data.get('age'))
        breed = int(request.data.get('breed'))  # Foreign key with Breed DB
        gender = request.data.get('gender')
        color = request.data.get('color')
        favoritefood = request.data.get('favoritefood')
        favoritetoy = request.data.get('favoritetoy')

        if (Breed.objects.filter(pk = breed).exists()):
            breed = Breed.objects.get(pk = breed)
        else:
            return Response({'success':False, 'error': 'Breed does not exist'}, status = status.HTTP_400_BAD_REQUEST)

        newDog = Dog(
            name = name,
            age = age,
            breed = breed,
            gender = gender,
            color = color,
            favoritefood = favoritefood,
            favoritetoy = favoritetoy
        )

        try:
            newDog.clean_fields()
        except Exception as e:
            print (e)
            return Response({'success':False, 'error':e}, status = status.HTTP_400_BAD_REQUEST)

        #Log event to DB
        newDog.save()
        return Response({'success': True}, status = status.HTTP_200_OK)


class DogDetails(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, pk, *args, **kwargs):
        dog = Dog.objects.filter(pk = pk)
        json_data = serializers.serialize('json', dog)
        return HttpResponse(json_data, content_type = 'json')

    def put(self, request, pk,  *args, **kwargs):
        dog = Dog.objects.get(pk = pk)

        if (request.data.get('name')):
            dog.name = request.data.get('name')
        if (request.data.get('age')):
            dog.age = int(request.data.get('age'))
        if (request.data.get('breed')):
            breed = request.data.get('breed')
            if (Breed.objects.filter(pk = pk).exists()):
                dog.breed = Breed.objects.get(pk = int(breed))
            else:
                return Response({'success':False, 'error': 'Breed does not exist'}, status = status.HTTP_400_BAD_REQUEST)
        if (request.data.get('gender')):
            dog.gender = request.data.get('gender')
        if (request.data.get('color')):
            dog.color = request.data.get('color')
        if (request.data.get('favoritefood')):
            dog.favoritefood = request.data.get('favoritefood')
        if (request.data.get('favoritetoy')):
            dog.favoritetoy = request.data.get('favoritetoy')

        try:
            dog.clean_fields()
        except Exception as e:
            print (e)
            return Response({'success':False, 'error':e}, status = status.HTTP_400_BAD_REQUEST)

        #Log event to DB
        dog.save()
        return Response({'success': True}, status = status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        if (Dog.objects.filter(pk = pk).exists()):
            Dog.objects.get(pk = pk).delete()
            return Response({'success': True}, status = status.HTTP_204_NO_CONTENT)
