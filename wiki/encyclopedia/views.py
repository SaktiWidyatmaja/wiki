from django.shortcuts import render, redirect
from . import util
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
    query = query_dict.get("q")
    entry_exist=[]

    for entry in entries:
        if query == entry:
            return redirect(f"/wiki/{query}")
    
    for entry in entries:
        if query in entry:
            entry_exist += [entry]
    
    return (request, "encyclopedia/search.html", {"entries" : entry_exist})