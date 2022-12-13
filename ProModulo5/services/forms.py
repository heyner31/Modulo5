from dataclasses import field
from tkinter import Widget
from turtle import textinput
from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from services.models import Service, Pedido


class PedidoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request',None)
        total_float = self.request.session.get('total_float')
        super().__init__(*args, **kwargs)
        self.fields['total'].initial = total_float
    
    class Meta:
        model = Pedido
        fields = ['nombre', 'direccion', 'colonia','correo', 'total']
        widgets = {
            'nombre':TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'direccion':TextInput(attrs={'class':'form-control', 'placeholder': 'Direccion'}),
            'colonia':TextInput(attrs={'class':'form-control', 'placeholder': 'Colonia'}),
            'correo':EmailInput(attrs={'class':'form-control', 'placeholder': 'Correo'}),
            'total':TextInput(attrs={'class':'form-control', 'readonly': 'readonly'}),
        }

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