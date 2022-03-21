from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegistrationSerializer



# Create your views here.

class CreateUser(generics.CreateAPIView):
    serializer_class = RegistrationSerializer



