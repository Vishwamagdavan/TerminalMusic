from django.shortcuts import render
from django.conf import settings
import os
# Create your views here.
def index(request):
    path = settings.MEDIA_ROOT
    song_list = os.listdir(path + '/')
    song_list=song_list[0]
    print(song_list)
    context={'url': song_list}
    return render(request,'index.html',context)