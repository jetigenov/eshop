# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from core.models import Setting, ContactMessage


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'updated', 'status']


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'updated', 'status']
    readonly_fields = ('name', 'subject', 'email', 'message', 'ip', 'phone')
    list_filter = ['status']

admin.site.register(Setting, SettingAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)
