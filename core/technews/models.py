from django.db import models
from common.models import BaseContent


class TechNews(BaseContent):
    CATEGORY_CHOICES = (
        ('ai', 'AI'),
        ('blockchain', 'Blockchain'),
        ('robotics', 'Robotics'),
        ('startups', 'Startups'),
        ('general', 'General'),
    )

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    news_source = models.CharField(max_length=200, blank=True)
    external_link = models.URLField(blank=True)

    class Meta:
        verbose_name = "Tech News"
        verbose_name_plural = "Tech News"
