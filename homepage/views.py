from django.views import generic
from django.shortcuts import render

import datetime

def index(request) :
    context = {
            'dt' : datetime.datetime.now().strftime('%b %d, %Y'),
            }
    return render(request, 'homepage/index.html', context)


def about(request):
    context = { 
            'dt' : datetime.datetime.now().strftime('%b %d, %Y'),
            }
    return render(request, 'homepage/about.html', context)


def testing_space(request) :
    context = {
        'dt' : datetime.datetime.now().strftime('%b %d, %Y'),
    }
    return render(request, 'homepage/testingspace.html', context)
