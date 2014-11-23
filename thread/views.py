from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotAllowed
from django.views.generic import ListView
from django.contrib.auth.models import User

from datetime import datetime
import json

from thread.models import Thread, Message
from registration.views import LoginForm

def index(request):
    return HttpResponseRedirect('/') if not request.user.is_authenticated() else render(request, 'thread/index.html', {
        'threads' : Thread.objects.filter(people__pk=request.user.pk),
    })


def read_thread(request, thread_id):
    return HttpResponseRedirect('/') if not request.user.is_authenticated() else render(request, 'thread/detail.html', {
        'js_files'  : ["/static/thread/js/thread.js"],
        'thread'    : Thread.objects.get(pk=thread_id),
        'messages'  : Message.objects.filter(thread=thread_id),
    })

def create_message(request, thread_id):
    body = json.loads(request.body.decode(encoding='UTF-8'))
    message = Message(text=body["messageBody"], thread=Thread(id=thread_id), author=User(id=request.user.id), timestamp=datetime.now())
    message.save()
    return HttpResponse('', None, 201)

def method_dispatch(**table):
    def invalid_method(request, *args, **kwargs):
        return HttpResponseNotAllowed(table.keys())

    def callable(request, *args, **kwargs):
        handler = table.get(request.method, invalid_method)
        return handler(request, *args, **kwargs)
    
    return callable
