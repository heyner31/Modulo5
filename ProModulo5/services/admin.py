from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
    ordering = ('title', 'created')
    search_fields = ('title', 'subtitle', 'pricing')
    list_display = ('title','subtitle','pricing','updated','created')
    list_filter = ('pricing',)

admin.site.register(Service, ServiceAdmin)
