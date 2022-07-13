from django.urls import path, include
from . import views as citizen_views

app_name = 'CitizenApp'
urlpatterns = [
    path('profile/', citizen_views.CitizenProfile, name='CitizenProfile'),
    path('login/', citizen_views.CitizenLogin, name='CitizenLogin'),
    path('logout/', citizen_views.CitizenLogout, name='CitizenLogout'),
]
