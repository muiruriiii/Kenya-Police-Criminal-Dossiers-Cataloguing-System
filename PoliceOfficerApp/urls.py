from django.urls import path, include
from . import views as officer_views


urlpatterns = [
    path('', officer_views.index, name='OfficerDashboard'),
    path('OfficersDisplay/', officer_views.OfficersDisplay, name='OfficersDisplay'),
    path('CitizensDisplay/', officer_views.CitizensDisplay, name='CitizensDisplay'),
    path('CrimesDisplay/', officer_views.CrimesDisplay, name='CrimesDisplay'),
    path('CriminalsDisplay/', officer_views.CriminalsDisplay, name='CriminalsDisplay'),
    path('login/', officer_views.login, name='OfficerLogin'),
    path('logout/', officer_views.OfficerLogout, name='OfficerLogout')
]