from django.urls import path

from . import views

app_name="encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("random/", views.rndm, name="random"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("save/", views.save, name="save")
]
