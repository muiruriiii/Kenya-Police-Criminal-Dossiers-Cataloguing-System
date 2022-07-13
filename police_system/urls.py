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
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('evidence/',record_views.evidence, name='evidence'),
    path('CitizenLogin/', record_views.CitizenLogin, name='CitizenLogin'),
    path('CitizenLogout/', record_views.CitizenLogout, name='CitizenLogout'),
    path('crimereport/',record_views.crimereport, name='crimereport'),
    path('casetracking/',record_views.casetracking, name='casetracking'),



    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
         name='password_reset'),

    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
         name='password_reset_done'),

    path('password_reset_confirm/<slug:uidb64>/<slug:token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
         name='password_reset_confirm'),

    path('password_reset_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
         name='password_reset_complete'),


    path('casetransfer/', record_views.casetransfer, name='casetransfer'),
    path('caseapproval/', record_views.caseapproval, name='caseapproval'),
    path('requestforms/', record_views.requestforms, name='requestforms'),
    path('signup/',record_views.signup, name='userSignUp'),
    path('',record_views.landingpage, name='index'),
    path('citizen/', include('CitizenApp.urls'), name='citizen'),
    path('policeofficer/', include('PoliceOfficerApp.urls'), name='policeofficer')
]
