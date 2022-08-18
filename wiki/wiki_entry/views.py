from django.http import HttpResponse
from django.shortcuts import render
from encyclopedia import util
from markdown2 import Markdown

# Create your views here.

def title(request, title) :
    return render(request, "wiki_entry/title.html", {
        "title" : title, "entry": (Markdown().convert((util.get_entry(title)))).replace('"','')
    })

def index(request):
    return render(request, "wiki_entry/index.html")