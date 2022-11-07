from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Notes


class ListNotes(ListView):
    model = Notes
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'


class DetailNoteView(DetailView):
    model = Notes
    context_object_name = 'note'