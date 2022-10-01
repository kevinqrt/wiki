from ast import If
from email import message
from http.client import HTTPResponse
from pickle import GET
from this import d
from tkinter import E, N, Entry
from turtle import title
from venv import create
from django.shortcuts import render

import markdown
import random

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
def saveedit(request):
    
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html", {
            "entryTitle" : title,
            "entry": markdown.markdown(content)
        })

def editentry(request):
    
    if request.method == 'POST':
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/editentry.html", {
            "title" : title,
            "content": content
    })


def search(request):
    q = request.POST['q']
    entries = util.list_entries()
    entrysubstring = []

    for entry in entries:
        if q.lower() == entry.lower():
            entryPage = util.get_entry(entry)
            return render(request, "encyclopedia/entry.html", {
                "searched": q,
                "entry": markdown.markdown(entryPage),
                "entryTitle": entry
            })
        elif q.lower() in entry.lower():
                entrysubstring.append(entry)


    return render(request, "encyclopedia/searchnotsuccess.html", {
        "entrysubstring": entrysubstring
    })

def createpage(request):

    if request.method == "POST":
        entries = util.list_entries()
        title = request.POST['title']
        content = request.POST['content']
        
        # check if encyclopedia already exists
        for entry in entries:
            if entry == title:
                return render(request, "encyclopedia/alreadyexists.html", {
        })
        
        # create encyclopedia from form
        with open("entries/" + title + '.md', 'w+') as f:
            f.truncate()
            f.write("#" + title + '\n' + content)
            f.close()

        entryPage = util.get_entry(title)
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown.markdown(entryPage),
            "entryTitle": title
        })

    return render(request, "encyclopedia/createpage.html", {

    })

def randompage(request):

    entries = util.list_entries()
    title = random.choice(entries)
    content = util.get_entry(title)

    return render(request, "encyclopedia/entry.html", {
        "entry": markdown.markdown(content),
        "entryTitle": title
    })