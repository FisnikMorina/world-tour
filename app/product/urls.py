from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("addtour/",views.tour_add_view, name="add-tour"),
    path("newtouradded/",views.new_tour_added, name="new-tour-added"),
]
