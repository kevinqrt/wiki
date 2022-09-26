from ast import If
from email import message
from http.client import HTTPResponse
from pickle import GET
from tkinter import E, Entry
from django.shortcuts import render

import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    entryPage = util.get_entry(entry)
    if entryPage == None:
        return render(request, "encyclopedia/doesnotexists.html", {
            "entryTitle": entry
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown.markdown(entryPage),
            "entryTitle": entry
        })


def search(request):
    q = request.POST['q']
    entries = util.list_entries()
    entrysubstring = []

    for entry in entries:
        if q == entry:
            entryPage = util.get_entry(entry)
            return render(request, "encyclopedia/entry.html", {
                "searched": q,
                "entry": markdown.markdown(entryPage),
                "entryTitle": entry
            })
        elif q in entry:
                entrysubstring.append(entry)

    return render(request, "encyclopedia/searchnotsuccess.html", {
        "entrysubstring": entrysubstring
    })

def createpage(request):


    return render(request, "encyclopedia/createpage.html", {
        
    })
