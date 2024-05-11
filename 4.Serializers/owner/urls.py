from django.urls import path, include
from rest_framework import routers
from .views import OwnerListCreateAPIView, OwnerRetrieveUpdateDestroyAPIView,TenListCreateAPIView,TenRetrieveUpdateDestroyAPIView
# from .views import OwnerCreateAPIView

urlpatterns = [
    path('owners/', OwnerListCreateAPIView.as_view()),
    path('ten/', TenListCreateAPIView.as_view()),
    path('owners/<int:pk>',OwnerRetrieveUpdateDestroyAPIView.as_view()),
    path('ten/<int:pk>', TenRetrieveUpdateDestroyAPIView.as_view()),
    # path('ownerten/',OwnerCreateAPIView.as_view()),
]

