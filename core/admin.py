# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from core.models import Setting


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'updated', 'status']


admin.site.register(Setting, SettingAdmin)
