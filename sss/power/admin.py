from django.contrib import admin

from .models import Human, Hobby


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

