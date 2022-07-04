from django.shortcuts import render, redirect


def index(request):
    if 'citizenID' in request.session:
        return render(request, 'CitizenApp/citizenProfile.html')
    else:
        return redirect(request, 'records/index.html')
# Create your views here.
