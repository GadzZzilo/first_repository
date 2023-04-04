from django.contrib import admin

from .models import Human, Hobby, Service, Developer, Feedback


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo']
    list_display_links = ['name', 'photo']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'create_at']
    list_display_links = ['name']
