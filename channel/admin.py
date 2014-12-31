from channel.models import Channel, Message
from django.contrib import admin

class ChannelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',   {'fields': ['name']}),
        ('Users',   {'fields': ['users']}),
    ]

    list_display = ('name','get_users_names')

class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Channel',   {'fields': ['channel']}),
        ('Posted by',   {'fields': ['op']}),
        ('Text',   {'fields': ['text']}),
        ('Timestamp',   {'fields': ['timestamp']}),
    ]

    list_display = ('channel', 'op', 'timestamp')

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Message, MessageAdmin)