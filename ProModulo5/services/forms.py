from dataclasses import field
from tkinter import Widget
from turtle import textinput
from django import forms
from django.forms import ModelForm, TextInput
from services.models import Service

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['title','subtitle', 'content', 'image', 'pricing']
        widgets = {
            'title':TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'subtitle':TextInput(attrs={'class':'form-control', 'placeholder':'Subtítulo'}),
        }

    def clean(self):
        super(ServiceForm, self).clean()
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            self._errors['title'] = self.error_class(['Mínimo 5 caracteres'])
        return self.cleaned_data