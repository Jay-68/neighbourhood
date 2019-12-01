# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=60)
    hood_location = models.CharField(max_length=60)
    occupants = models.IntegerField(default=0)

    def __str__(self):
      return self.hood_name