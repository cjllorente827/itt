from django.shortcuts import render
from django.http import HttpResponseRedirect

from channel.models import Channel, Message
from channel import controller, api

def index(request):
    return HttpResponseRedirect('/') if not request.user.is_authenticated() else render(
        request, 
        'channel/index.html', {
            'js_files'  : [ "/static/channel/js/channel.js", 
                            "/static/channel/js/tabs.js" ],
            'channels' : controller.get_user_channels(request.user.id),
        })

def view_channel(request, channel_id):
    return HttpResponseRedirect('/') if not request.user.is_authenticated() else render(
        request, 
        'channel/view_channel.html', {
            'js_files'  : [ "/static/channel/js/channel.js", 
                            "/static/channel/js/tabs.js" ],
            'channel'    : controller.get_channel(channel_id),
            'messages'  : controller.get_channel_messages(channel_id, 10),
        })

