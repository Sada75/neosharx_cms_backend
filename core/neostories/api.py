from rest_framework import serializers, viewsets
from .models import NeoStory


class NeoStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NeoStory
        fields = "__all__"


class NeoStoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NeoStory.objects.filter(status="published")
    serializer_class = NeoStorySerializer
    lookup_field = "slug"
