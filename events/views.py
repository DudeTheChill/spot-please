from django.shortcuts import render



def event_choices(request):
    return render(request, 'events/event_create_choices.html')