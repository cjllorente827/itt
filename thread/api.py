from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from thread.models import Message
from thread import controller

def read_thread(request, thread_id):
    return render(
        request, 
        'thread/read_thread.html', {
            'thread'    : controller.get_thread(thread_id),
            'messages'  : controller.get_thread_messages(thread_id, 10),
        })

def read_thread_messages(request, thread_id):
    return render(
        request, 
        'thread/read_thread_messages.html', {
            'messages'  : controller.get_thread_messages(thread_id, 10),
    })

def create_message(request):
    message = Message.create_from_request(request)
    message.save()
    return HttpResponse(read_thread_messages(request, message.thread.id), None, 201)