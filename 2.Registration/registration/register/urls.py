from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('register/',views.register),
    # path('data/',views.data)
]