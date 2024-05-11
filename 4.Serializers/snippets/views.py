from rest_framework import viewsets
from .models import Snippet
from .serializers import SnippetSerializers

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializers

