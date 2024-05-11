from  .models import Ten, Owner
from .serializers import OwnerTenSerializer,OwnerSerializer, TenSerializer
from rest_framework import generics
from rest_framework.response import Response
# from rest_framework.

class OwnerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class TenListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ten.objects.all()
    serializer_class = TenSerializer

class TenRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateAPIView):
    queryset = Ten.objects.all()
    serializer_class = TenSerializer


# class OwnerTenCreateAPIView(generics.CreateAPIView):
#     serializer_class = OwnerTenSerializer