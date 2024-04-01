from django.shortcuts import render,redirect
from pytube import *
from django.views.generic import View

def utube(request):
    data = {}
    if request.method == 'POST':
        link = request.POST.get('link')
        video = YouTube(link)
        stream = video.streams.filter(progressive = True).order_by('resolution').desc()
        selected_resolution = request.POST.get('select')
        if selected_resolution is not None:
            selected_video = stream.get_by_resolution(selected_resoltuion)
            if selected_video:
                selected_video.download(output_path='../../Downloads')
                
        # fin_vid = stream[selected_video]

        data = {
            'url' : link,
            'videos' : stream,
            'selected_videos' : selected_resolution
        }
        return render(request,'index.html',data)
    return render(request,'index.html')


# def utube(request):
#     if request.method == 'POST':
#         link = request.POST['link']
#         video = YouTube(link)
#         stream = video.streams.get_highest_resolution()
#         stream.download()
#     return render(request,'index.html')