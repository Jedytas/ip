from django import forms
from .models import Artist, Painting, Gallery

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'biography']

class PaintingForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = ['title', 'description', 'artist', 'creation_date']

class PaintingForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = ['title', 'description', 'artist', 'creation_date']
