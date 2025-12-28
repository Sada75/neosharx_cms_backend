from django.db import models
from django.utils.text import slugify


class BaseContent(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)

    short_description = models.TextField(max_length=500)
    content = models.TextField()

    cover_image = models.ImageField(
        upload_to='covers/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    published_at = models.DateTimeField(blank=True, null=True)

    # SEO
    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-published_at', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
