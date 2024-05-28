from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title','description','start_time','end_time', 'timezone')
    search_fields = ('timezone',)

admin.site.register(Event, EventAdmin)