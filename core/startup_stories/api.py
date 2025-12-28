from rest_framework import serializers, viewsets
from .models import StartupStory


class StartupStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupStory
        fields = "__all__"


class StartupStoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StartupStory.objects.filter(status="published")
    serializer_class = StartupStorySerializer
    lookup_field = "slug"
