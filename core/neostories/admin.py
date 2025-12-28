from django.contrib import admin
from .models import NeoStory


@admin.register(NeoStory)
class NeoStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'story_type', 'status')
    list_filter = ('story_type', 'status')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
