"""police_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from records import views as record_views
from django.conf import settings
from django.conf.urls.static import static

app_name='PoliceSystem'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('evidence/',record_views.evidence, name='evidence'),
    path('crimereport/', record_views.CrimeListDisplay, name='crimereport'),
    path('issueforms/', record_views.issueforms, name='issueforms'),
    path('signup/',record_views.signup, name='userSignUp'),
    path('',record_views.landingpage, name='index'),
    path('citizen/', include('CitizenApp.urls'), name='citizen'),
    path('policeofficer/', include('PoliceOfficerApp.urls'), name='policeofficer')
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
