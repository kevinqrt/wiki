from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search/", views.search, name="search-result"),
    path("create/", views.createpage, name="create"),
    path("editentry/", views.editentry, name="editentry"),
    path("saveedit", views.saveedit, name="saveedit"),
    path("randompage", views.randompage, name="randompage"),
]
