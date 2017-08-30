from django.shortcuts import render
from django.http import HttpResponse

from .models import Officer

officers_order = {
        "Pres": 0,
        "Vice": 1,
        "Mark": 2,
        "Outr": 3,
        "Secr": 4,
        "Trea": 5,
        "Webm": 6
}

# Create your views here.
def index(request):
    officers = Officer.objects.all()

    officers_list = len(officers_order)*[None]
    for officer in officers:
        idf = officer.position[:4]
        pos = officers_order[idf]
        officers_list[pos] = officer

    context = {'officers_list': officers_list}
    return render(request, 'officers/index.html', context)

