from django.http import HttpResponse
from .models import Notes
from .models import Items
from django.shortcuts import render


def home(request):
    notes = Notes.objects.all()
    items = Items.objects.all()
    return render(request, 'note.html',
                  {'notes': notes, 'items': items})