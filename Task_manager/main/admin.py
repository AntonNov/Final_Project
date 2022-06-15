from django.contrib import admin

from .models import *


class MainAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'date_name', 'is_executed')
    list_editable = ('date', 'date_name', 'is_executed')
    list_filter = ('date', 'date_name', 'is_executed')


admin.site.register(Task, MainAdmin)
