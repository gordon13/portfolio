from django.shortcuts import render
from django.template import RequestContext

def index(request):

    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {

        })
    )

def page2(request):

    return render(
        request,
        'app/page2.html',
        context_instance = RequestContext(request,
        {

        })
    )