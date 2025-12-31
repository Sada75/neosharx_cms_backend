from django.contrib import admin
from .models import StartupStory
from common.storage import upload_to_supabase

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

    def save_model(self, request, obj, form, change):
        if "cover_image" in request.FILES:
            obj.cover_image = upload_to_supabase(
                request.FILES["cover_image"],
                folder="startupstories"
            )
        super().save_model(request, obj, form, change)
