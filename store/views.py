import imp
from django.shortcuts import render
from django.http import HttpResponse
from store.models import books

# Create your views here.

def home(request):
    items = books.objects.all()
    param={'items':items}
    return render(request, 'store.html', param)
