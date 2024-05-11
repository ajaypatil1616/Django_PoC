from django.urls import path
from .views import SnippetViewSet

urlpatterns = [
    path('sn/', SnippetViewSet.as_view({'get': 'list', 'post': 'create'}), name='snippet-list'),
    path('sn/<int:pk>/', SnippetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='snippet-detail'),
]
