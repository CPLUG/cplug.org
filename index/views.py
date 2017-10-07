from django.shortcuts import render
from .models import Event, Officer

# Create your views here.
def index(request):
    events = Event.objects.all()
    officers = Officer.objects.all()

    context = {'officers_list': officers, 'events': events}
    return render(request, 'index/index.html', context)
