from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from records.models import Citizen as CitizenModel, CrimeList as CrimeListModel, Crime as CrimeModel
from records.models import Crime
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from police_system.helpers.tokens import *


def evidence(request):
    return render(request, 'records/evidence.html', {'title': 'Evidence'})


def CrimeListDisplay(request):
    crimelist = CrimeListModel.objects.all()
    if request.method == 'POST':
        if request.POST.get('crimeID') and request.POST.get('crimeDescription'):
                saverecord = CrimeModel()
                saverecord.crimeID = CrimeListModel.objects.get(crimeID=request.POST.get('crimeID')).pk
                saverecord.description = request.POST.get('crimeDescription')

                #Here we check if a citizen is logged in so that we can decide whether the crime has been reported anonymously or not.
                if 'citizenID' in request.session:
                    saverecord.citizenID = request.session['citizenID']
                    try:
                        saverecord.save()
                    except Exception as e:
                        messages.error(request, e)
                        return render(request, 'records/crimereport.html')
                    else:
                        messages.success(request, 'Crime has been reported successfully!')
                        return render(request, "records/crimereport.html", {"crimelists":crimelist})
                else:
                    try:
                        saverecord.save()
                    except Exception as e:
                        messages.error(request, e)
                        return render(request, 'records/crimereport.html')
                    else:
                        messages.success(request, 'Crime has been reported successfully!')
                        return render(request, "records/crimereport.html", {"crimelists":crimelist})
        else:
            messages.error(request, 'An error has occurred')
            #return render(request, "records/crimereport.html", {"crimelists": crimelist})
    else:
        return render(request, "records/crimereport.html", {"crimelists":crimelist})



def casetracking(request):
    return render(request, 'records/casetracking.html', {'title': 'Case Tracking '})


def casetransfer(request):
    return render(request, 'records/casetransfer.html', {'title': 'Case Transfer '})


def caseapproval(request):
    return render(request, 'records/caseapproval.html', {'title': 'Case Approval '})


def issueforms(request):
    return render(request, 'records/issueforms.html', {'title': 'Issue Forms '})


def signup(request):
    if request.method == 'POST':
        if request.POST.get('regFName') and\
                request.POST.get('regLName') and\
                request.POST.get('regEmail') and\
                request.POST.get('regPhone') and\
                request.POST.get('regPassword') and\
                request.POST.get('regConPassword') and\
                request.POST.get('regIDNo') and\
                request.POST.get('regGender') and \
                request.FILES['citizenImage'] and \
                request.POST.get('regAddress'):
            # If the password and confirm password are same then the data will be saved in the database else an error message will be sent
            if request.POST.get('regPassword') == request.POST.get('regConPassword'):
                #Getting the image that has been uploaded
                fileStorage = FileSystemStorage()
                citizenImage = request.FILES['citizenImage']

                saverecord = CitizenModel()
                saverecord.fName = request.POST.get('regFName')
                saverecord.lName = request.POST.get('regLName')
                saverecord.email = request.POST.get('regEmail')
                saverecord.tel = request.POST.get('regPhone')

                #Hash password before recording in the DB
                saverecord.password = make_password(request.POST.get('regPassword'))
                saverecord.nationalID = request.POST.get('regIDNo')
                saverecord.gender = request.POST.get('regGender')
                saverecord.address = request.POST.get('regAddress')
                try:
                    saverecord.save()
                    citizenID = saverecord.pk
                    citizenImageName = 'citizen-%s%s' % (citizenID, '.jpg')
                    fileStorage.save('%s' % citizenImageName, citizenImage)
                    saverecord.citizenImage = citizenImageName
                    saverecord.save()
                except IntegrityError as e:
                    messages.error(request, e)
                    return render(request, 'records/signup.html')
                else:
                    messages.success(request, 'Record Saved Successfully...!')
                    return redirect('CitizenApp:CitizenLogin')
            else:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'records/signup.html')
    else:
        return render(request, 'records/signup.html', {'title': 'Sign Up'})


def dashboard(request):
    return render(request, 'records/dashboard.html', {'title': 'Dashboard'})


def landingpage(request):
    return render(request, 'records/index.html', {'title': 'Landing Page', 'pageId': 8})
