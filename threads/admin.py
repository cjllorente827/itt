from threads.models import Thread, Strand
from django.contrib import admin

class ThreadAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Topic',   {'fields': ['topic']}),
        ('People',   {'fields': ['people']}),
    ]

    list_display = ('topic','get_people_names')

class StrandAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Thread id',   {'fields': ['thread_id']}),
        ('Posted by',   {'fields': ['poster']}),
        ('Text',   {'fields': ['text']}),
        ('Timestamp',   {'fields': ['timestamp']}),
    ]

    list_display = ('thread_id', 'poster')

admin.site.register(Thread, ThreadAdmin)
admin.site.register(Strand, StrandAdmin)