from django.shortcuts import render
from .models import Event, Officer

officers_order = {
        "Pres": 0,
        "Vice": 1,
        "Comm": 2,
        "Mark": 3,
        "Outr": 4,
        "Secr": 5,
        "Trea": 6,
        "Webm": 7
}

# Create your views here.
def index(request):
    events = Event.objects.all()
    officers = Officer.objects.all()

    officers_list = len(officers_order)*[None]
    for officer in officers:
        idf = officer.position[:4]
        pos = officers_order[idf]
        officer.first = officer.name.split()[0].lower()
        officers_list[pos] = officer

    context = {'officers_list': officers_list, 'events': events}
    return render(request, 'index/index.html', context)
