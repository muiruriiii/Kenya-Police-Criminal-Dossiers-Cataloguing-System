from django.urls import path, include
from . import views as citizen_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'CitizenApp'
urlpatterns = [
    path('profile/', citizen_views.CitizenProfile, name='CitizenProfile'),
    path('login/', citizen_views.CitizenLogin, name='CitizenLogin'),
    path('logout/', citizen_views.CitizenLogout, name='CitizenLogout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)