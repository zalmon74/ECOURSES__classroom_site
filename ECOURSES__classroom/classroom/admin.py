from django.contrib import admin
from rangefilter.filters import DateRangeFilterBuilder

from .models import ContactusModel


@admin.register(ContactusModel)
class ContactusAdminModel(admin.ModelAdmin):
    
    list_display = ('id', 'subject', 'name', 'email', 'sent_date')
    list_display_links = ('subject', 'name', 'email')
    
    readonly_fields = (
        'id', 
        'name', 
        'email', 
        'phone_number',
        'subject', 
        'message', 
        'sent_date'
    )
    
    list_filter = (('sent_date', DateRangeFilterBuilder()),)
