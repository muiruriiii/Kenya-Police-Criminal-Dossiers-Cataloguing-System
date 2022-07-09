from django.urls import path, include
from . import views as citizen_views

app_name = 'CitizenApp'
urlpatterns = [
    path('', citizen_views.index, name='CitizenProfile'),

]
