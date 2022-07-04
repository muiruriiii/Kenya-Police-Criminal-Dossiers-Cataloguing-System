from django.urls import path, include
from . import views as citizen_views


urlpatterns = [
    path('', citizen_views.index, name='CitizenProfile'),

]
