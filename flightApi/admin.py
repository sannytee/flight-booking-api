"""Register your models here """
from django.contrib import admin

from .models.flight import Flight
from .models.user import User


class UserAdmin(admin.ModelAdmin):
    """ Customize superadmin's users view."""
    search_fields = ('email',)
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ('admin', 'staff')

    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Primary information', {
            'fields': (
                'first_name', 'last_name', 'profile_picture'
            )
        }),
        ('Advanced Option', {
            'fields': ('admin', 'staff')
        })
    )


admin.site.register(User, UserAdmin)
admin.site.register(Flight)
