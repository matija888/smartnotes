from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.ListNotes.as_view()),
    path('notes/<int:pk>', views.DetailNoteView.as_view(0)),
]
