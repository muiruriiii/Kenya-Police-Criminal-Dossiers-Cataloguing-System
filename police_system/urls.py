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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from records import views as record_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('policeofficer/', record_views.policeofficer, name='policeofficer'),
    path('criminalbooking/',record_views.criminalbooking, name='criminalbooking'),
    path('evidence/',record_views.evidence, name='evidence'),
   path('login/',record_views.login, name='login'),
   path('crimereport/',record_views.crimereport, name='crimereport'),
   path('casetracking/',record_views.casetracking, name='casetracking'),
   path('ob/',record_views.ob, name='ob'),
   path('signup/',record_views.signup, name='signup'),
   path('landingpage/',record_views.landingpage, name='landingpage'),
   path('dashboard/',record_views.dashboard, name='dashboard'),

]
