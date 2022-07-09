from django.shortcuts import render, redirect

from records.views import landingpage


def index(request):
    if 'citizenID' in request.session:
        return render(request, 'CitizenApp/citizenProfile.html')
    else:
        return redirect(landingpage)
# Create your views here.
