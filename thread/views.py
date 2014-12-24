from django.shortcuts import render
from django.http import HttpResponseRedirect

from thread.models import Thread, Message
from thread import controller

def index(request):
    return HttpResponseRedirect('/') if not request.user.is_authenticated() else render(
        request, 
        'thread/index.html', {
            'js_files'  : [ "/static/thread/js/thread.js", 
                            "/static/thread/js/tabs.js" ],
            'threads' : controller.get_user_threads(request.user.pk),
        })

def view_thread(request, thread_id):
    return HttpResponseRedirect('/') if not request.user.is_authenticated() else render(
        request, 
        'thread/view_thread.html', {
            'js_files'  : [ "/static/thread/js/thread.js", 
                            "/static/thread/js/tabs.js" ],
            'thread'    : controller.get_thread(thread_id),
            'messages'  : controller.get_thread_messages(thread_id, 10),
        })

