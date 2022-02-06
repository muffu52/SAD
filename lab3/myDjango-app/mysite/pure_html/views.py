from django.shortcuts import render
from teammate.models import Teammate
from json import dumps

def interval(request):
    return render(request, 'interval.html')

def homework(request):
    members = list(Teammate.objects.all())
    names = []
    for m in members:
        name = f"{m.id}. {m.title} {m.first_name} {m.last_name}"
        names.append(name)
    data = dumps(names)
    return render(request, 'homework.html',{"data": data})

def home(request):
    return render(request, 'home.html')

def button(request):
    return render(request, 'button.html')
