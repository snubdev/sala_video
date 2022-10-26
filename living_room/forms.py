from django import forms
from .models import Room


class RoomForm(forms.Form):
    class Meta:
        model = Room
        fields = ['title', 'video']