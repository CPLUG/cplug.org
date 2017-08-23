from django.shortcuts import render
from django.http import HttpResponse

from .models import Officer

# Create your views here.
def index(request):
    officers = Officer.objects.all()
    context = {'officers_list': officers}
    return render(request, 'officers/index.html', context)

