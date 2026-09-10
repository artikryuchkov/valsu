from django.contrib import admin

from .models import FormSubmission


@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('username', 'submitted_at', 'ip_address', 'source')
    readonly_fields = ('username', 'submitted_at', 'ip_address', 'source')
    search_fields = ('username', 'ip_address', 'source')
    list_filter = ('submitted_at',)

    def has_add_permission(self, request):
        return False
