from django.urls import path 
from . import views


app_name="wiki_entry"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name="title")
]