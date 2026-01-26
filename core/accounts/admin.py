from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "auth_provider", "is_verified", "is_staff")
    search_fields = ("email", "username")
    list_filter = ("auth_provider", "is_verified", "is_staff")
