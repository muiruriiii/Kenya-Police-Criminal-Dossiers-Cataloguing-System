from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from records.models import Officer as OfficerModel, Crime as CrimeModel, Criminal as CriminalModel, Citizen as CitizenModel


def index(request):
    return render(request, 'PoliceOfficerApp/index.html', {'title': 'Police Dashboard'})


def login(request):
    if 'citizenID' in request.session:
        del request.session['citizenID']
        return render(request, 'records/CitizenLogin.html', {'title': 'Police Login'})
    elif 'officerID' in request.session:
        return redirect(index)
    else:
        if request.method == "POST":
            if request.POST.get('loginEmail') and request.POST.get('loginPassword'):
                loginEmail = request.POST.get('loginEmail')
                loginPassword = request.POST.get('loginPassword')
                officer = OfficerModel.objects.get(email=loginEmail)

                if check_password(loginPassword, officer.password):
                    # TODO create single variable that stores individual column of the citizen table.
                    request.session['officerID'] = officer.id
                    request.session['officerName'] = officer.fName

                    return redirect(index)
                else:
                    messages.error(request, 'Passwords do not match')
                    return render(request, 'records/CitizenLogin.html', {'title': 'Police Login'})
        return render(request, 'records/CitizenLogin.html', {'title': 'Police Login'})


def OfficerLogout(request):
    try:
        del request.session['officerID']
    except Exception as e:
        messages.error(request, e)
    else:
        messages.success(request, 'Logged out.')
        return render(request, 'records/CitizenLogin.html', {'title': 'Police Login'})


def OfficersDisplay(request):
    officers = OfficerModel.objects.all()
    context = {'officers': officers}
    return render(request, 'PoliceOfficerApp/OfficersDisplay.html', context)


def CriminalsDisplay(request):
    criminals = CriminalModel.objects.all()
    context = {'criminals': criminals}
    return render(request, 'PoliceOfficerApp/CriminalsDisplay.html', context)


def CitizensDisplay(request):
    citizens = CitizenModel.objects.all()
    context = {'citizens': citizens}
    return render(request, 'PoliceOfficerApp/CitizensDisplay.html', context)


def CrimesDisplay(request):
    crimes = CrimeModel.objects.all()
    context = {'crimes': crimes}
    return render(request, 'PoliceOfficerApp/CrimesDisplay.html', context)