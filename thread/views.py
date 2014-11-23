from django.shortcuts import render
from django.http import HttpResponseRedirect

from thread.models import Thread, Message

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

