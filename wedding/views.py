from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def accomodations(request):
    return render(request, 'accomodations.html')

def registry(request):
    return render(request, 'registry.html')

def rsvp(request):
    return render(request, 'rsvp.html')
