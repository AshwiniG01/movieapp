from django import forms
from movieapp.models import MovieTable

class MovieDataTable(forms.ModelForm):
    class Meta:
        model = MovieTable
        fields = '__all__'
    