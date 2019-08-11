from django.shortcuts import render


def index(request):
    return render(request, 'autotag/index.html', {})
