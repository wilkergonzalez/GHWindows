from django.shortcuts import render
from .models import Owner, Cat

from django.shortcuts import get_object_or_404

from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

