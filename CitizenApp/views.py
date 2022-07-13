from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect

from records.views import landingpage
from records.models import Citizen as CitizenModel


def CitizenProfile(request):
    if 'citizenID' in request.session:
        citizen = CitizenModel.objects.get(id=request.session['citizenID'])
        return render(request, 'CitizenApp/citizenProfile.html',{'citizen':citizen})
    else:
        return redirect('CitizenApp:CitizenLogin')


def CitizenLogin(request):
    if request.method == "POST":
        if request.POST.get('loginEmail') and request.POST.get('loginPassword'):
            loginEmail = request.POST.get('loginEmail')
            loginPassword = request.POST.get('loginPassword')
            citizen = CitizenModel.objects.get(email=loginEmail)

            if check_password(loginPassword, citizen.password):
                #TODO create single variable that stores individual column of the citizen table.
                request.session['citizenID'] = citizen.id
                request.session['citizenName'] = citizen.fName+' '+citizen.lName

                #currentCitizen = CitizenClass(citizen.id,citizen.fName,citizen.lName,citizen.email,citizen.tel,citizen.password,citizen.nationalID,citizen.gender,citizen.address)

                #return render(request, 'records/CitizenLogin.html')
                return redirect(landingpage)
            else:
                messages.error(request, 'Passwords do not match')
                return render(request, 'records/CitizenLogin.html', {'title': 'Login'})
    else:
        return render(request, 'records/CitizenLogin.html', {'title': 'Login'})


def CitizenLogout(request):
    try:
        del request.session['citizenID']
    except Exception as e:
        messages.error(request, e)
    else:
        messages.error(request, 'Logged out.')
        return redirect('/', {'title':'Landing Page', 'pageId': 8})
