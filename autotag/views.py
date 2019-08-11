
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from static.autotag import autotag

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')


def index(request):
    return render(request, 'autotag/index.html', {})


@csrf_exempt
def predict(request):
    #img_data = str(request.FILES['file'])
    img_data = request.FILES['file'].read()

    labels = autotag(img_data)

    #return render(request, 'autotag/predict.html', {'labels': labels})
    return JsonResponse({'labels': labels})
