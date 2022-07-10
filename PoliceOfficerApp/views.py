from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.template.defaulttags import url

from records.models import Officer as OfficerModel, Crime as CrimeModel, Criminal as CriminalModel, Citizen as CitizenModel



def index(request):
    if 'officerID' not in request.session:
        return redirect('PoliceOfficerApp:OfficerLogin')
    else:
        return render(request, 'PoliceOfficerApp/index.html', {'title': 'Police Dashboard', 'pageID': 1})


def login(request):
    if 'citizenID' in request.session:
        del request.session['citizenID']
        return render(request, 'records/CitizenLogin.html', {'title': 'Police Login'})
    elif 'officerID' in request.session:
        return redirect('PoliceOfficerApp:OfficerDashboard')
    else:
        if request.method == "POST":
            if request.POST.get('loginEmail') and request.POST.get('loginPassword'):
                loginEmail = request.POST.get('loginEmail')
                loginPassword = request.POST.get('loginPassword')
                officer = OfficerModel.objects.get(email=loginEmail)

                if check_password(loginPassword, officer.password):
                    # TODO create single variable that stores individual column of the citizen table.
                    request.session['officerID'] = officer.id
                    request.session['officerName'] = officer.fName + ' ' + officer.lName

                    return redirect('PoliceOfficerApp:OfficerDashboard')
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
        return redirect('PoliceOfficerApp:OfficerLogin')


def OfficerProfile(request):
    if 'officerID' not in request.session:
        return redirect('PoliceOfficerApp:OfficerLogin')
    else:
        officer = OfficerModel.objects.get(id=request.session['officerID'])
        context = {'officer': officer, 'pageID': 6, 'title': 'Officer Profile'}
        return render(request, 'PoliceOfficerApp/OfficerProfile.html', context)


def OfficersDisplay(request):
    if 'officerID' not in request.session:
        return redirect('PoliceOfficerApp:OfficerLogin')
    else:
        officers = OfficerModel.objects.all()
        context = {'officers': officers, 'pageID': 2, 'title': 'List of Officers'}
        return render(request, 'PoliceOfficerApp/OfficersDisplay.html', context)


def CriminalsDisplay(request):
    if 'officerID' not in request.session:
        return redirect('PoliceOfficerApp:OfficerLogin')
    else:
        criminals = CriminalModel.objects.all()
        context = {'criminals': criminals, 'pageID': 4, 'title': 'Criminals Display'}
        return render(request, 'PoliceOfficerApp/CriminalsDisplay.html', context)


def CitizensDisplay(request):
    if 'officerID' not in request.session:
        return redirect('PoliceOfficerApp:OfficerLogin')
    else:
        citizens = CitizenModel.objects.all()
        context = {'citizens': citizens, 'pageID': 3, 'title': 'Citizen Display'}
        return render(request, 'PoliceOfficerApp/CitizensDisplay.html', context)


def CrimesDisplay(request):
    if 'officerID' not in request.session:
        return redirect('PoliceOfficerApp:OfficerLogin')
    else:
        crimes = CrimeModel.objects.all()
        context = {'crimes': crimes, 'pageID': 5, 'title': 'Crime Display'}
        return render(request, 'PoliceOfficerApp/CrimesDisplay.html', context)

