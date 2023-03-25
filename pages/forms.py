from django import forms
from .models import Page, NotificationConfig


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Orden'})
        }
        labels = {
            'title': '',
            'content': '',
            'order': '',
        }

class HermesForm(forms.ModelForm):
    class Meta:
        model = NotificationConfig
        fields = ['name', 'day']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'day': forms.CheckboxSelectMultiple(attrs={'class': ' form-check-inline', 'style': 'margin-left: 30px'}),
        }
        choices = [
            ('Lunes', 'Lunes'),
            ('Martes', 'Martes'),
            ('Miercoles', 'Miércoles'),
            ('Jueves', 'Jueves'),
            ('Viernes', 'Viernes'),
            ('Sabado', 'Sábado'),
            ('Domingo', 'Domingo'),
        ]

    name = forms.CharField(max_length=30, widget=Meta.widgets['name'])
    day = forms.MultipleChoiceField(choices=Meta.choices, widget=Meta.widgets['day'])

