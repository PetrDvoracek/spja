from django import forms
from .models import Song,Album,Band


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ('name', 'description')

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'release_date', 'num_stars', 'description', 'band')

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('name', 'album')