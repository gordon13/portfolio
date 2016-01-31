from django.shortcuts import render
from django.template import RequestContext

from models import Piece, Skill, Software

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

def about(request):

    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {

        })
    )

def skills(request):
    software = Software.objects.all()
    skills_obj = Skill.objects.all()
    return render(
        request,
        'app/skills.html',
        context_instance = RequestContext(request,
        {
            'skills_obj':skills_obj,
            'software':software
        })
    )