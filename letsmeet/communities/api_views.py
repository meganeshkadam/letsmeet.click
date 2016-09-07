from rest_framework import viewsets

from .models import Community
from .serializers import CommunitySerializer


class CommunityView(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
