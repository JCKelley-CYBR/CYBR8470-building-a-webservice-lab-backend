
from django.urls import include, re_path, path
#Django Rest Framework
from rest_framework import routers
from api import controllers
from django.views.decorators.csrf import csrf_exempt
from api.views import *

#REST API routes
#router = routers.DefaultRouter(trailing_slash=False)

#urlpatterns = [
#    re_path(r'^', include(router.urls)),
#    path('dogs/', csrf_exempt(controllers.DogList.as_view())),
#    path('dogs/<int:pk>', csrf_exempt(controllers.DogDetails.as_view())),
#    path('breeds/', csrf_exempt(controllers.BreedsList.as_view())),
#    path('breeds/<int:pk>', csrf_exempt(controllers.BreedDetails.as_view()))
#]

#Viewset Routes
router = routers.DefaultRouter(trailing_slash=False)
router.register('dogs', DogViewSet, basename = 'dog')
router.register('breeds', BreedViewSet, basename = 'breed')

urlpatterns = [
    re_path(r'^', include(router.urls)),
    #path('dogs/<int:pk>', include(router.urls, 'DogViewSet.retrieve'))
]
