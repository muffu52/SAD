from django.shortcuts import render
from django.http import HttpResponse

def interval_index(request):
    return render(request,'interval.html')

def homework_index(request):
    return render(request,'homework.html')

def button_index(request):
    return render(request,'button.html')

def get_home(request):
    return render(request,'home.html')

