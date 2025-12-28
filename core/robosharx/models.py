from django.db import models
from common.models import BaseContent


class RoboSharxArticle(BaseContent):
    CATEGORY_CHOICES = (
        ('robotics', 'Robotics'),
        ('ai', 'AI'),
        ('automation', 'Automation'),
        ('research', 'Research'),
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    reference_links = models.TextField(blank=True)

    class Meta:
        verbose_name = "RoboSharx Article"
        verbose_name_plural = "RoboSharx Articles"
