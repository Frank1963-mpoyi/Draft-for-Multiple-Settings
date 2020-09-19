from django.shortcuts import render
from .models import Music


def gospel_music(request):
    queryset = Music.objects.all()
    #art =Music.objects.filter(artiste__endswith='l')
    obj = Music.objects.get(id=1)
    template_name = 'draft_app/gospel.html' 
    context = { 
        'arta':queryset,
        'obj': obj,
        }
    return render(request, template_name, context)


