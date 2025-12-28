from django.contrib import admin
from .models import NeosharxTalk


@admin.register(NeosharxTalk)
class NeosharxTalkAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'speaker_name',
        'talk_type',
        'status',
        'published_at',
    )

    list_filter = ('status', 'talk_type')
    search_fields = ('title', 'speaker_name')
    prepopulated_fields = {'slug': ('title',)}
