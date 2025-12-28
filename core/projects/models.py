from django.db import models
from common.models import BaseContent


class NeoProject(BaseContent):
    PROJECT_STATUS_CHOICES = (
        ('idea', 'Idea'),
        ('development', 'Development'),
        ('beta', 'Beta'),
        ('live', 'Live'),
        ('paused', 'Paused'),
    )

    project_status = models.CharField(
        max_length=20,
        choices=PROJECT_STATUS_CHOICES,
        default='idea'
    )

    # Core description
    about_project = models.TextField()
    problem_statement = models.TextField(blank=True)
    solution_overview = models.TextField(blank=True)

    # Team & ownership
    project_lead = models.CharField(max_length=150)
    team_members = models.TextField(
        blank=True,
        help_text="Comma-separated names"
    )

    # Tech & links
    technology_stack = models.JSONField(default=list, blank=True)
    repository_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)

    # Progress & timeline
    start_date = models.DateField(blank=True, null=True)
    expected_release_date = models.DateField(blank=True, null=True)
    progress_percentage = models.PositiveIntegerField(
        default=0,
        help_text="0 to 100"
    )

    class Meta:
        verbose_name = "Neo Project"
        verbose_name_plural = "Neo Projects"
