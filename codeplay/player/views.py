from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import os
from bs4 import BeautifulSoup
from pytube import YouTube

# Create your views here.
def index(request):
    url="https://www.youtube.com/results?search_query="
    data={}
    if request.method=='POST':
        text=request.POST.get('text')
        print(text)
        data['text']=url+text
        return JsonResponse(data,safe=False)
    path = settings.MEDIA_ROOT
    song_list = os.listdir(path + '/')
    song_list=song_list[0]
    context={'url': song_list}
    return render(request,'index.html',context)