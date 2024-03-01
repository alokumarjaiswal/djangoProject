from django.shortcuts import render
from db.models import University

# Create your views here.


def index(request):
    university_list = University.objects.all()
    return render(request,
                  'db/model.html',
                  {'universities': university_list})
