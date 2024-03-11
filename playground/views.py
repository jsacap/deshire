from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    context = {
        'name': 'Jun'
    }
    return render(request, 'hello.html', context)

# Create your views here.
