from django.contrib import admin
from .models import TechNews


@admin.register(TechNews)
class TechNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status')
    list_filter = ('category', 'status')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
