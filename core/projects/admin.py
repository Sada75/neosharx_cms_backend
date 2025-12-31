from django.contrib import admin
from .models import NeoProject
from common.storage import upload_to_supabase

@admin.register(NeoProject)
class NeoProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'project_status',
        'project_lead',
        'progress_percentage',
        'status',
    )

    list_filter = ('project_status', 'status')
    search_fields = ('title', 'project_lead')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ("Basic Info", {
            "fields": (
                "title",
                "slug",
                "short_description",
                "cover_image",
                "status",
                "published_at",
            )
        }),
        ("Project Details", {
            "fields": (
                "project_status",
                "about_project",
                "problem_statement",
                "solution_overview",
            )
        }),
        ("Team & Tech", {
            "fields": (
                "project_lead",
                "team_members",
                "technology_stack",
            )
        }),
        ("Links & Progress", {
            "fields": (
                "repository_url",
                "live_demo_url",
                "progress_percentage",
                "start_date",
                "expected_release_date",
            )
        }),
        ("SEO", {
            "fields": (
                "seo_title",
                "seo_description",
            )
        }),
    )

    def save_model(self, request, obj, form, change):
        if "cover_image" in request.FILES:
            obj.cover_image = upload_to_supabase(
                request.FILES["cover_image"],
                folder="neoprojects"
            )
        super().save_model(request, obj, form, change)
