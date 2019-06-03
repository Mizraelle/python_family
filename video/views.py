from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Comment
from django.template.context_processors import csrf


def hello(request):
    response = {}
    response.update(csrf(request))
    response['videos'] = Video.objects.all()
    response['comments'] = Comment.objects.all()
    return render(request, 'index.html', response)


def form(request):
    print(request.GET)
    print(request.POST)
    return redirect('/video/hello/')

def onevideo(request, slug):
    response = {}
    response.update(csrf(request))
    response['videos'] = [Video.objects.get(slug=slug)]
    response['comments'] = Comment.objects.filter(video_id=response['videos'][0].id)
    return render(request, 'index.html', response)


def add_like(request):
    v = Video.objects.get(id=int(request.GET['id'][4:]))
    v.likes_video += 1
    v.save()
    return HttpResponse(v.likes_video)
# Create your views here.
