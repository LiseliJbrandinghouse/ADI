import os
from django.shortcuts import render

from adi import settings
from .models import Event
from datetime import datetime
from .models import Speaker
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from decimal import Decimal


def home(request):
    event = Event.objects.first()  # Fetch the event to display in the countdown section
    return render(request, 'index.html', {'event': event})

def speakers_view(request):
    speakers = Speaker.objects.all()
    return render(request, 'speakers.html', {'speakers': speakers})

def speakers(request):
    return render(request, 'speakers.html')

def registration(request):
    return render(request, 'registration.html')

def vote(request):
    return render(request, 'voting.html')


def documents(request):
    return render(request, 'documents.html')

def media(request):
    return render(request, 'media.html')
def accommodation(request):
    return render(request, 'accommodation.html')
def fife(request):
    return render(request, 'fife.html')
def outcome(request):
    return render(request, 'outcome.html')



def donate(request):
    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount'))
        currency = request.POST.get('currency')
        # Process the donation
        # You can add more logic here for handling donations
        return redirect('donation_success')
    return render(request, 'donate.html')
