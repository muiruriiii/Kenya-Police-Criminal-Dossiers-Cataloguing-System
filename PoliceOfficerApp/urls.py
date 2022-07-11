from django.urls import path, include
from . import views as officer_views

app_name = "PoliceOfficerApp"
urlpatterns = [
    path('', officer_views.index, name='OfficerDashboard'),
    path('OfficersDisplay/', officer_views.OfficersDisplay, name='OfficersDisplay'),
    path('OfficerProfile/', officer_views.OfficerProfile, name='OfficerProfile'),
    path('CitizensDisplay/', officer_views.CitizensDisplay, name='CitizensDisplay'),
    path('CrimesDisplay/', officer_views.CrimesDisplay, name='CrimesDisplay'),
    path('criminalbooking/', officer_views.criminalbooking, name='criminalbooking'),
    path('CriminalsDisplay/', officer_views.CriminalsDisplay, name='CriminalsDisplay'),
    path('login/', officer_views.login, name='OfficerLogin'),
    path('ob/', officer_views.ob, name='ob'),

# CriminalEdit and update paths
    path('EditCriminal/<int:id>', officer_views.CriminalEdit, name='CriminalEdit'),
    #path('update/<int:id>', officer_views.update, name='update'),

    path('OfficerRegister/', officer_views.OfficerRegister, name='OfficerRegister'),
    path('logout/', officer_views.OfficerLogout, name='OfficerLogout')
]
