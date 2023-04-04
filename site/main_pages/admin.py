from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Service, Developer, Feedback


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_html_photo']
    list_display_links = ['name', 'get_html_photo']
    prepopulated_fields = {'slug': ('name',)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Фото'


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'create_at']
    list_display_links = ['name']
