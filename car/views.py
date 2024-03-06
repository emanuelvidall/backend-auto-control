from rest_framework import generics
from django.shortcuts import render
from .models import User, Vehicle, Expense
from .serializers import UserSerializer, VehicleSerializer, ExpenseSerializer
from rest_framework.response import Response

class UserListCreateView(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserUpdateView(generics.RetrieveUpdateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  partial = True

class UserDeleteView(generics.DestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def destry(self, request, *args, **kwargs):
    instance = self.get_object()
    instance.delete()
    return Response(print("Deleted User"))
