from django.urls import path
from . import views

urlpatterns = [
    path("", views.notes_list_create, name="notes_list_create"),
    path("<int:pk>/", views.note_detail, name="note_detail"),
]
