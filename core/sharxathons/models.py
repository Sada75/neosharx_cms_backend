from django.db import models
from common.models import BaseContent


class Sharxathon(BaseContent):
    HACKATHON_TYPE_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('hybrid', 'Hybrid'),
    )

    hackathon_type = models.CharField(
        max_length=20,
        choices=HACKATHON_TYPE_CHOICES
    )

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    registration_deadline = models.DateTimeField()

    location = models.CharField(max_length=200, blank=True)
    prize_pool = models.CharField(max_length=100, blank=True)
    registration_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Sharxathon"
        verbose_name_plural = "Sharxathons"
