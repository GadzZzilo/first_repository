from django.contrib import admin

from .models import User, EmailVerification

admin.site.register(User)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'created', 'expiration']
    readonly_fields = ['created', 'expiration']
