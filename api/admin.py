from django.contrib import admin

#if ENVIRONMENT == 'PROD':
#	from api.models import *
#else:
from api.models import *

# Register your models here.
# Admin Models
class DogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy')
    list_display_links = ('id', 'name')

class BreedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')
    list_display_links = ('id', 'name')

# Normal Models
admin.site.register(Dog, DogAdmin)
admin.site.register(Breed, BreedAdmin)
