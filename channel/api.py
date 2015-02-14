from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from datetime import datetime

from channel.models import Message
from channel import controller

NUM_MESSAGES = 150

def read_channel(request, channel_id):
    return render(
        request, 
        'channel/read_channel.html', {
            'channel'    : controller.get_channel(channel_id),
            'messages'  : controller.get_channel_messages(channel_id, NUM_MESSAGES),
        })

def read_channel_messages(request, channel_id):
    return render(
        request, 
        'channel/read_channel_messages.html', {
            'messages'  : controller.get_channel_messages(channel_id, NUM_MESSAGES),
    })

def read_new_channel_messages(request, channel_id, timestamp):
    new_messages = controller.get_new_channel_messages(channel_id, NUM_MESSAGES, datetime.fromtimestamp(float(timestamp)/1e3))
    return render(
        request, 
        'channel/read_channel_messages.html', {
            'messages'  : new_messages,
    }) if new_messages is not None else HttpResponse('', None, 304)

def create_message(request):
    message = Message.create_from_request(request)
    message.save()
    return HttpResponse(read_channel_messages(request, message.channel.id), None, 201)