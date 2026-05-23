from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extras', {
            'fields': ('curso', 'bio')
        }),
    )

admin.site.register(Profile, CustomUserAdmin)