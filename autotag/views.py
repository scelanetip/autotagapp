
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from static.autotag import autotag, autotag_video, autotag_txt, detect_document

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
IMG_EXTENSION = ['.bmp', '.jpe', '.jpg', '.jpeg', '.tif', '.gif', '.ppm', '.rgb', '.pgm', '.png', '.pnm']
VID_EXTENSION = ['.mpeg', '.mov', '.mpg', '.mpe', '.avi', '.movie', '.mp4']


def index(request):
    return render(request, 'autotag/index.html', {})


@csrf_exempt
def predict(request):

    data = request.FILES['file'].read()
    filename, file_extension = os.path.splitext(request.FILES['file'].name)
    labels = ['vinals']
    if file_extension in IMG_EXTENSION:
        labels = labels + ['imagen'] + detect_document(data) + autotag(data)
    elif file_extension in VID_EXTENSION:
        labels = labels + ['video'] + autotag_video(data) + autotag_txt(data)
    else:
        labels = ['not valid file extension']

    return JsonResponse({'labels': labels})
