# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Neighbourhood(models.Model):
    name = models.CharField(max_length=90)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    occupants = models.IntegerField(null=True, default=0)

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls, neighbourhood_id):
        neighbourhood = cls.objects.get(id=neighbourhood_id)
        return neighbourhood

    def update_neighbourhod(self, name):
        self.name = name
        self.save()

    def update_occupants(self, occupants):
        self.occupants = occupants
        self.save()

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=30)
    neighbourhood = models.ForeignKey(
        Neighbourhood, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True)
    email = models.EmailField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
