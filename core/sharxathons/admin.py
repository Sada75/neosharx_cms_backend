from django.contrib import admin
from .models import Sharxathon
from common.storage import upload_to_supabase

@admin.register(Sharxathon)
class SharxathonAdmin(admin.ModelAdmin):
    list_display = ('title', 'hackathon_type', 'start_date', 'status')
    list_filter = ('hackathon_type', 'status')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if "cover_image" in request.FILES:
            obj.cover_image = upload_to_supabase(
                request.FILES["cover_image"],
                folder="sharxathons"
            )
        super().save_model(request, obj, form, change)
