from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('name')
            email = form.cleaned_data['email']
            print(nombre,email)
            dominio = email[email.find('@')+1:]
            if dominio != 'gmail.com':
                form.add_error('email', 'Dominio invalido')
                form.add_error('email', 'Solo es permitido gmail')
                return render(request, 'contact/contact.html', {'form':form})

            return HttpResponseRedirect(reverse_lazy('contact:thanks'))

    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form':form})

def thanks(request):
    return render(request, 'contact/thanks.html')


