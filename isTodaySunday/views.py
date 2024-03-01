from django.shortcuts import render
import datetime

# Create your views here.


def isTodaySunday(request):
    today = datetime.datetime.now().strftime('%A')
    return render(request, 'isTodaySunday/isTodaySunday.html', {'today': today})