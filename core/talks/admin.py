from django.contrib import admin
from .models import NeosharxTalk
from common.storage import upload_to_supabase

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

    def save_model(self, request, obj, form, change):
        if "cover_image" in request.FILES:
            obj.cover_image = upload_to_supabase(
                request.FILES["cover_image"],
                folder="talks"
            )
        super().save_model(request, obj, form, change)
