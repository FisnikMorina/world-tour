from django import forms
from django.contrib.auth.models import User

class TourForm(forms.Form):
    origin_country = forms.CharField(max_length=48)
    destination_country = forms.CharField(max_length=48)
    number_of_nights = forms.IntegerField()
    price = forms.IntegerField()


