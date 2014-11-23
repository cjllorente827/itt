from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from thread.models import Thread, Message

def read_thread(request, thread_id):
    return render(
        request, 
        'thread/read_thread.html', {
            'thread'    : Thread.objects.get(pk=thread_id),
            'messages'  : Message.objects.filter(thread=thread_id),
        })

def read_thread_messages(request, thread_id):
    return render(
        request, 
        'thread/read_thread_messages.html', {
            'messages'  : Message.objects.filter(thread=thread_id),
    })

def create_message(request):
    message = Message.create_from_request(request)
    message.save()
    return HttpResponse(read_thread_messages(request, message.thread.id), None, 201)

