from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Breed(models.Model):
    name = models.CharField(
        default = 'Australian Shepherd',
        max_length = 25
    )
    size = models.CharField(
        default = 'Medium',
        max_length = 6,
        choices = [
            ("TINY", "Tiny"),
            ("SMALL", "Small"),
            ("MEDIUM", "Medium"),
            ("LARGE", "Large"),
        ]
    )
    friendliness = models.IntegerField(
        default = 5,
        validators = [
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    trainability = models.IntegerField(
        default = 5,
        validators = [
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    sheddingamount = models.IntegerField(
        default = 5,
        validators = [
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    exerciseneeds = models.IntegerField(
        default = 5,
        validators = [
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return str(self.breed)


class Dog(models.Model):
    name = models.CharField(
        default = 'Reese',
        max_length = 25
    )
    age = models.IntegerField(
        default = 1
    )
    breed = models.ForeignKey(
        Breed,
        on_delete = models.CASCADE
    )
    gender = models.CharField(
        max_length = 6,
        default = "Female"
    )
    color = models.CharField(
        max_length = 25,
        default = "Red Merle"
    )
    favoritefood = models.CharField(
        max_length = 25,
        default = "Twizzlers"
    )
    favoritetoy = models.CharField(
        max_length = 25,
        default = "Frisbee"
    )

    def __str__(self):
        return str(self.dogs)
