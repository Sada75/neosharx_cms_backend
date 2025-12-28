from django.db import models
from common.models import BaseContent


class NeoStory(BaseContent):
    STORY_TYPE_CHOICES = (
        ('innovation', 'Innovation'),
        ('personal', 'Personal'),
        ('research', 'Research'),
        ('vision', 'Vision'),
    )

    story_type = models.CharField(
        max_length=20,
        choices=STORY_TYPE_CHOICES
    )

    author_name = models.CharField(max_length=150, blank=True)
    reading_time_minutes = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "NeoStory"
        verbose_name_plural = "NeoStories"
