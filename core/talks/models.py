from django.db import models
from common.models import BaseContent


class NeosharxTalk(BaseContent):
    TALK_TYPE_CHOICES = (
        ('podcast', 'Podcast'),
        ('interview', 'Interview'),
        ('panel', 'Panel Discussion'),
    )

    speaker_name = models.CharField(max_length=150)
    speaker_designation = models.CharField(max_length=150, blank=True)
    speaker_company = models.CharField(max_length=150, blank=True)

    talk_type = models.CharField(
        max_length=20,
        choices=TALK_TYPE_CHOICES
    )

    video_url = models.URLField(blank=True)
    duration_minutes = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Neosharx Talk"
        verbose_name_plural = "Neosharx Talks"
