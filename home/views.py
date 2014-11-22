from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from account.views import renderSideBar

class HomeIndexView(TemplateView):

    template = 'itt/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {
        'sidebar' : renderSideBar(request),
    })

