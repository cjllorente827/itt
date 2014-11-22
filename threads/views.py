from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView

from threads.models import Thread, Strand
from account.views import renderSideBar

def index(request):
    template = 'threads/index.html'
    threads = Thread.objects.filter(people__pk=request.user.pk)
    return render(request, template, {
        'threads' : threads,
        'sidebar' : renderSideBar(request),
    })

def detail(request, thread_id):
    template = 'threads/detail.html'
    thread = Thread.objects.get(pk=thread_id)
    strands = Strand.objects.filter(thread_id=thread_id)
    return render(request, template, {
        'js'      : '<script src="/threads/threadMonitor.js"></script>',
        'thread'  : thread,
        'strands' : strands,
        'sidebar' : renderSideBar(request),
    })