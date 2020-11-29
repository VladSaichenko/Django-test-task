from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from url_filter.integrations.drf import DjangoFilterBackend

from apps.api.permissions.memory import IsOwnerOrReadOnly
from apps.memories.models import Memory
from apps.memories.serializers.memories import MemorySerializer


class MemoryView(viewsets.ModelViewSet):
    serializer_class = MemorySerializer
    queryset = Memory.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user',)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
