from django.contrib import admin
from .models import Sharxathon


@admin.register(Sharxathon)
class SharxathonAdmin(admin.ModelAdmin):
    list_display = ('title', 'hackathon_type', 'start_date', 'status')
    list_filter = ('hackathon_type', 'status')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
