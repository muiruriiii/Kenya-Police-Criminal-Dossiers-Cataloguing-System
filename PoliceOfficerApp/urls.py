from django.urls import path, include
from . import views as officer_views
from django.conf import settings
from django.conf.urls.static import static

app_name = "PoliceOfficerApp"
urlpatterns = [
    path('', officer_views.index, name='OfficerDashboard'),
    path('OfficersDisplay/', officer_views.OfficersDisplay, name='OfficersDisplay'),
    path('OfficerProfile/', officer_views.OfficerProfile, name='OfficerProfile'),
    path('CitizensDisplay/', officer_views.CitizensDisplay, name='CitizensDisplay'),
    path('CrimesDisplay/', officer_views.CrimesDisplay, name='CrimesDisplay'),
    path('criminalbooking/', officer_views.criminalbooking, name='criminalbooking'),
    path('CriminalsDisplay/', officer_views.CriminalsDisplay, name='CriminalsDisplay'),
    path('CrimeListDisplay/', officer_views.CrimeListDisplay, name='CrimeListDisplay'),

    path('login/', officer_views.login, name='OfficerLogin'),
    path('ob/<int:id>', officer_views.ob, name='ob'),
    # path('upload/', officer_views.upload, name='upload'),
    path('addCrimes/', officer_views.addCrimes, name='addCrimes'),

    # CriminalEdit and update paths
    path('EditCriminal/<int:id>', officer_views.CriminalEdit, name='CriminalEdit'),

    path('EditOfficer/<int:id>', officer_views.OfficerEdit, name='OfficerEdit'),
    path('OfficerRegister/', officer_views.OfficerRegister, name='OfficerRegister'),
    path('logout/', officer_views.OfficerLogout, name='OfficerLogout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)