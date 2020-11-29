from rest_framework import serializers

from apps.memories.models import Memory


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ('id', 'user', 'title', 'text', 'longitude', 'latitude', 'created',)

        extra_kwargs = {
            'user': {'read_only': True},
            'created': {'read_only': True},
        }
