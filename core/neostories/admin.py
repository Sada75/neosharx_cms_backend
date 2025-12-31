from django.contrib import admin
from .models import NeoStory
from common.storage import upload_to_supabase

@admin.register(NeoStory)
class NeoStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'story_type', 'status')
    list_filter = ('story_type', 'status')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if "cover_image" in request.FILES:
            obj.cover_image = upload_to_supabase(
                request.FILES["cover_image"],
                folder="neostories"
            )
        super().save_model(request, obj, form, change)
