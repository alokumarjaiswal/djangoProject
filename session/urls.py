from django.urls import path
from . import views


urlpatterns = [
    path('', views.num_visits, name = 'num_visits')
]