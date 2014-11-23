from thread.models import Thread, Message
from django.contrib import admin

class ThreadAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Topic',   {'fields': ['topic']}),
        ('People',   {'fields': ['people']}),
    ]

    list_display = ('topic','get_people_names')

class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Thread',   {'fields': ['thread']}),
        ('Posted by',   {'fields': ['author']}),
        ('Text',   {'fields': ['text']}),
        ('Timestamp',   {'fields': ['timestamp']}),
    ]

    list_display = ('thread', 'author')

admin.site.register(Thread, ThreadAdmin)
admin.site.register(Message, MessageAdmin)