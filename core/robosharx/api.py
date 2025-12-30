from rest_framework import viewsets, serializers
from .models import RoboSharxArticle


class RoboSharxArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoboSharxArticle
        fields = "__all__"


class RoboSharxArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RoboSharxArticle.objects.filter(status="published")
    serializer_class = RoboSharxArticleSerializer
    lookup_field = "slug"
