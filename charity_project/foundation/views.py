from django.shortcuts import render, get_object_or_404
from .models import Event, SuccessStory


def index(request):
    events = Event.objects.all()  # Получаем все мероприятия
    stories = SuccessStory.objects.all()  # Получаем все истории успеха
    return render(request, 'foundation/index.html', {'events': events, 'stories': stories})  # Передаем данные в шаблон

def contact(request):
    return render(request, 'foundation/contact.html')

def donation(request):
    return render(request, 'foundation/donation.html')

def initiative(request):
    return render(request, 'foundation/initiative.html')


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'foundation/event_detail.html', {'event': event})


def privacy_policy(request):
    return render(request, 'foundation/privacy_policy.html')

def terms_of_use(request):
    return render(request, 'foundation/terms_of_use.html')

