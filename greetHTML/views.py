from django.shortcuts import render


# Create your views here.

def greet_html(request, name):
    return render(request, 'greetHTML/greet.html', {'name': name.capitalize()})
