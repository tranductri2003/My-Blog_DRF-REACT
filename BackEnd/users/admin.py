from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name',
                   'avatar', 'first_name', 'first_name', 'about', 'is_active', 'is_staff')

    ordering = ('-start_date',)
    list_display = ('email', 'id', 'user_name', 'first_name',
                    'is_active', 'is_staff', 'num_post',
                    'num_view', 'num_like', 'num_comment')

    fieldsets = (
        (None, {'fields': ('email', 'user_name',
         'first_name', 'avatar', 'start_date')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups')}),
        ('Personal', {'fields': ('about', 'age', 'occupation', 'country')}),
        ('Statistics', {'fields': ('num_post',
         'num_view', 'num_like', 'num_comment',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
