from django.shortcuts import render, redirect
from . import util
from markdown2 import Markdown
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def rndm(request):
    entry=random.choice(util.list_entries())
    return redirect(f"/wiki/{entry}")

def search(request):
    entries = util.list_entries()
    query_dict = request.GET
    query = (query_dict.get("q")).lower()
    entry_exist=[]

    for entry in entries:
        if query == entry.lower():
            return redirect(f"/wiki/{entry}")
    
    for entry in entries:
        if query in entry.lower():
            entry_exist += [entry]
    
    return render(request, "encyclopedia/search.html", {"entries" : entry_exist})

def create(request):
    return render(request, "encyclopedia/create.html", {})

def save(request):
    wiki_dict = request.GET
    wiki_title = wiki_dict.get("wiki_title")
    wiki_content = f'# {wiki_title}\n{wiki_dict.get("wiki_content")}'
    util.save_entry(wiki_title, wiki_content)
    return render(request, "wiki_entry/title.html", {
        "title": wiki_title, "entry" : Markdown().convert(util.get_entry(wiki_title))
    })