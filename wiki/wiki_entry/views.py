from django.http import HttpResponse
from django.shortcuts import render
from encyclopedia import util
from markdown2 import Markdown

# Create your views here.

def title(request, title) :
    return render(request, "wiki_entry/title.html", {
        "title" : title, "entry": (Markdown().convert((util.get_entry(title))))
    })

def edit(request, title):
    return render(request, "wiki_entry/edit.html", {
        "title":title, "entry" : (util.get_entry(title)).split("\n",1)[1]
    })