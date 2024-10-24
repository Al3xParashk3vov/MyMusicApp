from django import forms

from MyMusicApp.mixins import PlaceholderMixin, ReadOnlyMixin
from albums.models import Album


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)

class AlbumCreateForm(PlaceholderMixin, AlbumBaseForm):
    pass

class AlbumEditForm(PlaceholderMixin, AlbumBaseForm):
    pass

class AlbumDeleteForm(ReadOnlyMixin, AlbumBaseForm):
    read_only_fields = ['album_name', 'artist', 'genre', 'description']
