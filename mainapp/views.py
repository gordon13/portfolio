from django.shortcuts import render
from django.template import RequestContext

from models import Piece

def index(request):
    pieces = Piece.objects.all()
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'pieces':pieces
        })
    )

def threedee(request):

    return render(
        request,
        'app/3d.html',
        context_instance = RequestContext(request,
        {

        })
    )

def skills(request):
    skills = None
    return render(
        request,
        'app/skills.html',
        context_instance = RequestContext(request,
        {
            'skills':skills
        })
    )