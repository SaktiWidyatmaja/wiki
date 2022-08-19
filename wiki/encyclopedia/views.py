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
    query = (query_dict.get("q")).lower()
    entry_exist=[]

    for entry in entries:
        if query == entry.lower():
            return redirect(f"/wiki/{entry}")
    
    for entry in entries:
        if query in entry.lower():
            entry_exist += [entry]
    
    return render(request, "encyclopedia/search.html", {"entries" : entry_exist})