from django.contrib import admin

from .models import Human, Hobby, Service, Developer


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'work', 'hobby', 'married', 'create_at']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


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

