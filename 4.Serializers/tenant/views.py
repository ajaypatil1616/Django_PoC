from django.shortcuts import render
from .models import Tenant
from .serializations import TenantSerilizations
from rest_framework import viewsets

class TenantAPIClass(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerilizations
