from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from datetime import datetime

from thread.models import Message
from thread import controller

def read_thread(request, thread_id):
    return render(
        request, 
        'thread/read_channel.html', {
            'thread'    : controller.get_thread(thread_id),
            'messages'  : controller.get_thread_messages(thread_id, 10),
        })

def read_thread_messages(request, thread_id):
    return render(
        request, 
        'thread/read_channel_messages.html', {
            'messages'  : controller.get_thread_messages(thread_id, 10),
    })

def read_new_thread_messages(request, thread_id, timestamp):
    new_messages = controller.get_new_thread_messages(thread_id, 10, datetime.fromtimestamp(float(timestamp)/1e3))
    return render(
        request, 
        'thread/read_channel_messages.html', {
            'messages'  : new_messages,
    }) if new_messages is not None else HttpResponse('', None, 304)

def create_message(request):
    message = Message.create_from_request(request)
    message.save()
    return HttpResponse(read_thread_messages(request, message.thread.id), None, 201)