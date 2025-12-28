from django.contrib import admin
from .models import StartupStory


@admin.register(StartupStory)
class StartupStoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'startup_name',
        'founder_name',
        'stage',
        'status',
    )
    list_filter = ('stage', 'status')
    search_fields = ('title', 'startup_name', 'founder_name')
    prepopulated_fields = {'slug': ('title',)}
