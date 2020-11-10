from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import os
from youtube_search import YoutubeSearch
from pytube import YouTube
from .models import Song
import json

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
        stream.download(mpath,filename='temp')
        data['text']=url+results[0]['url_suffix']
        data['track']=results[0]['title']
        data['tumbnails']=results[0]['thumbnails']
        data['duration']=results[0]['duration']
        data['views']=results[0]['views']
        with open('data.txt', 'w') as json_file:
            json.dump(data, json_file)
        return JsonResponse(data,safe=False)
    with open('data.txt','r') as f:
        data = json.load(f)
    track=data['track']
    thumbnails=data['tumbnails']
    views=data['views']
    link=data['text']
    path = settings.MEDIA_ROOT
    song_list = os.listdir(path + '/')
    if song_list:
        song_list=song_list[0]
    else:
        song_list=""
    context={'url': song_list,'track': track,'tumbnails':thumbnails,'views':views,'link':link}
    return render(request,'index.html',context)