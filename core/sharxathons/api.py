from rest_framework import serializers, viewsets
from .models import Sharxathon


class SharxathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sharxathon
        fields = "__all__"


class SharxathonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sharxathon.objects.filter(status="published")
    serializer_class = SharxathonSerializer
    lookup_field = "slug"
