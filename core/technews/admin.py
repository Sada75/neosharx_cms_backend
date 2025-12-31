from django.contrib import admin
from .models import TechNews
from common.storage import upload_to_supabase

@admin.register(TechNews)
class TechNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status')
    list_filter = ('category', 'status')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if "cover_image" in request.FILES:
            obj.cover_image = upload_to_supabase(
                request.FILES["cover_image"],
                folder="technews"
            )
        super().save_model(request, obj, form, change)
