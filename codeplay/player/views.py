from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import os
from youtube_search import YoutubeSearch
from pytube import YouTube
from .models import Song
# Create your views here.
mpath=settings.MEDIA_ROOT
def index(request):
    url="https://www.youtube.com/"
    data={}
    if request.method=='POST':
        text=request.POST.get('text')
        results = YoutubeSearch(text, max_results=10).to_dict()
        yt=YouTube(url+results[0]['url_suffix'])
        stream=yt.streams.filter(only_audio=True).first()
        file=stream.download(mpath,filename='temp')
        data['text']=url+results[0]['url_suffix']
        return JsonResponse(data,safe=False)
    path = settings.MEDIA_ROOT
    song_list = os.listdir(path + '/')
    if song_list:
        song_list=song_list[0]
    else:
        song_list=""
    context={'url': song_list}
    return render(request,'index.html',context)