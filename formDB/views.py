from django.shortcuts import render, redirect

from .forms import ContactForm

from .models import Contact


# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'formDB/success.html')
    else:
        form = ContactForm()

    return render(request, 'formDB/contact.html', {'form': form})


def display(request):
    contacts = Contact.objects.all()
    return render(request, 'formDB/display.html', {'contacts': contacts})