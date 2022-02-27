from django.shortcuts import render
from django.http import HttpResponse
from .models import Counter
from json import dumps

def home(request):
    value = list(Counter.objects.all())
    print(value)
    if len(value) == 0:
        print('mai mi')
        count = Counter()
        count.name = 'Counter'
        count.value = 0
        count.save()
    else:
        for m in value:
            context = {'id': m.id,'name': m.name, 'value': m.value}
            context = dumps(context)
    return render(request, 'home.html',{"data": context})

def get(request):
    # value = Counter.objects.all()
    id = request.GET.get('content')
    count = Counter.objects.get(pk=id)
    return HttpResponse(count.value)

def add(request):
    id = request.POST.get('content')
    count = Counter.objects.get(pk=id)
    count.value = count.value + 1
    count.save()
    return HttpResponse(id)

def reset(request):
    id = request.POST.get('content')
    count = Counter.objects.get(pk=id)
    count.value = 0
    count.save()
    return HttpResponse(id)
    