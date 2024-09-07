from django.shortcuts import render
from rest_framework import generics
from .models import Phone
from .serializers import PhoneSerializer
# Create your views here.


class PhoneListCreate(generics.ListCreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    lookup_field = "pk"