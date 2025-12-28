from rest_framework import serializers, viewsets
from .models import NeoProject


class NeoProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeoProject
        fields = "__all__"


class NeoProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NeoProject.objects.filter(status="published")
    serializer_class = NeoProjectSerializer
    lookup_field = "slug"
