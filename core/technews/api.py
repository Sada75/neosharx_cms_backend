from rest_framework import viewsets , serializers
from .models import TechNews



class TechNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechNews
        fields = "__all__"

class TechNewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TechNews.objects.filter(status="published").order_by("-created_at")
    serializer_class = TechNewsSerializer
    lookup_field = "slug"
