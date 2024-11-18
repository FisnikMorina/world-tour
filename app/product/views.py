from django.shortcuts import render, redirect
from .models import Tour
from .form import TourForm

def home(request):
    tour = Tour.objects.all()
    content = {"tours":tour}
    return render(request,"tours/home.html",content)


def tour_add_view(request):
    if request.method == "POST":
        form = TourForm(request.POST)
        if form.is_valid():
            new_tour = Tour(
                origin_country = form.cleaned_data["origin_country"],
                destination_country = form.cleaned_data["destination_country"],
                number_of_nights = form.cleaned_data["number_of_nights"],
                price = form.cleaned_data["price"],
            )
            new_tour.save()
            return redirect("new-tour-added")
    else:
        form = TourForm()
    content = {"form":form}
    return render(request, "tours/addtour.html", content)


def new_tour_added(request):
    return render(request, "tours/touradded.html")