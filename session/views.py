from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def num_visits(request):
    visits = request.session.get('num_visits', 0)
    visits += 1
    request.session['num_visits'] = visits
    return HttpResponse(f'Number of visits: {visits}')
