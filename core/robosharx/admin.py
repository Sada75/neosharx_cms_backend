from django.contrib import admin
from .models import RoboSharxArticle


@admin.register(RoboSharxArticle)
class RoboSharxAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status')
    list_filter = ('category', 'status')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
