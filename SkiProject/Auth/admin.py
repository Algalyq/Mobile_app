from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import PhoneOTP

admin.site.register(PhoneOTP)


User = get_user_model()
class UserAdmin(admin.ModelAdmin):
    
       
    class Meta:
        verbose_name_plural = "User"
    list_display = ('user_name', 'phone',  'standard',  'is_admin')
    list_filter = ('standard','is_staff','is_active' ,'is_admin', )
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('user_name', 'standard','score',)}),
        ('Permissions', {'fields': ('is_admin','is_staff','is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2')}
        ),
    )
    
    search_fields = ('phone','user_name')
    ordering = ('phone','user_name')
    filter_horizontal = ()
 


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)