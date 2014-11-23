from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotAllowed
from django.views.generic import ListView
from django.contrib.auth.models import User

from thread.models import Thread, Message
from registration.views import LoginForm

def index(request):
    return HttpResponseRedirect('/') if not request.user.is_authenticated() else render(
        request, 
        'thread/index.html', {
            'threads' : Thread.objects.filter(people__pk=request.user.pk),
        })

def view_thread(request, thread_id):
    return HttpResponseRedirect('/') if not request.user.is_authenticated() else render(
        request, 
        'thread/view_thread.html', {
            'js_files'  : ["/static/thread/js/thread.js"],
            'thread'    : Thread.objects.get(pk=thread_id),
            'messages'  : Message.objects.filter(thread=thread_id),
        })


def read_thread(request, thread_id):
    return HttpResponseRedirect('/') if not request.user.is_authenticated() else render(
        request, 
        'thread/read_thread.html', {
            'thread'    : Thread.objects.get(pk=thread_id),
            'messages'  : Message.objects.filter(thread=thread_id),
        })

def read_thread_messages(request, thread_id):
    return HttpResponseRedirect('/') if not request.user.is_authenticated() else render(
        request, 
        'thread/read_thread_messages.html', {
            'messages'  : Message.objects.filter(thread=thread_id),
    })


def create_message(request):
    message = Message.create_from_request(request)
    message.save()
    return HttpResponse(read_thread_messages(request, message.thread.id), None, 201)

