from django.urls import path 
from . import views


app_name="wiki_entry"
urlpatterns = [
    path("<str:title>", views.title, name="title"),
    path("<str:title>/edit", views.edit, name="edit")
]