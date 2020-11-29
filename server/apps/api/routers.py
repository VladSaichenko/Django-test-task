from rest_framework import routers

from apps.memories.viewsets.memories import MemoryView


router = routers.DefaultRouter()
router.register('memory', MemoryView, basename='memory')
