from django.contrib import admin
from .models import ContactInfo


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'working_hours', 'is_visible')
    list_filter = ('is_visible', )
    list_editable = ('is_visible',)
