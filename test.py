from pytube import YouTube

# creating YouTube object
yt = YouTube("https://www.youtube.com/watch?v=IQEDu8SPHao") 

# accessing audio streams of YouTube obj.(first one, more available)
stream = yt.streams.filter(only_audio=True).first()
# downloading a video would be: stream = yt.streams.first() 

# download into working directory
stream.download()