from rest_framework import serializers, viewsets
from .models import NeosharxTalk


class NeosharxTalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeosharxTalk
        fields = "__all__"


class NeosharxTalkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NeosharxTalk.objects.filter(status="published")
    serializer_class = NeosharxTalkSerializer
    lookup_field = "slug"
