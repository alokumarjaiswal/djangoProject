from django.shortcuts import render

from .forms import ContactForm


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
