from django.contrib import admin

from .models import Human


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'work', 'married', 'create_at']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}

