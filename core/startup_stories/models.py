from django.db import models
from common.models import BaseContent


class StartupStory(BaseContent):
    STAGE_CHOICES = (
        ('idea', 'Idea'),
        ('seed', 'Seed'),
        ('series_a', 'Series A'),
        ('growth', 'Growth'),
    )

    startup_name = models.CharField(max_length=200)
    founder_name = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES)

    key_learnings = models.TextField(blank=True)

    class Meta:
        verbose_name = "Startup Story"
        verbose_name_plural = "Startup Stories"
