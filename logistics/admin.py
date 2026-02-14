from django.contrib import admin
from .models import Ship, Voyage

# Register your models here.
@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Voyage)
class VoyageAdmin(admin.ModelAdmin):
    list_display = [
        'ship',
        'start_port',
        'destination_port',
        'start_date',
        'end_date'
    ]
    list_filter = ['ship', 'start_date']
    search_fields = ['start_port', 'destination_port']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'start_date'