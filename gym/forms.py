from django import forms
from .models import Event


class AddEventForm(forms.ModelForm):


    class Meta:
        model = Event
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
