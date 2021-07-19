# from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserList(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()


