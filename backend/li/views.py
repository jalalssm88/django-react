# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets          # add this
from .serializers import PhoneNumbersSerializer      # add this
from .models import PhoneNumbers                # add this

class PhoneNumbersView(viewsets.ModelViewSet):       # add this
    serializer_class = PhoneNumbersSerializer          # add this
    queryset = PhoneNumbers.objects.all()              # add this