from django.urls import path
from . import views

urlpatterns = [
    path('model/',views.modeltrials)
]