from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from records.models import Crime
from records.models import Citizen
from records.models import Criminal
from records.models import Officer


def policeOfficer(request):
    if request.method == 'POST':
        if request.POST.get('regFName') and \
                request.POST.get('regLName') and \
                request.POST.get('regEmail') and \
                request.POST.get('regPhone') and \
                request.POST.get('regRank') and \
                request.POST.get('regIDNo') and \
                request.POST.get('regGender') and \
                request.POST.get('regAddress'):
            saverecord = Officer()
            saverecord.fName = request.POST.get('regFName')
            saverecord.lName = request.POST.get('regLName')
            saverecord.email = request.POST.get('regEmail')
            saverecord.tel = request.POST.get('regPhone')
            saverecord.rank = request.POST.get('regRank')

            #default password is KenyaPolice2022
            saverecord.password = make_password('KenyaPolice2022')
            saverecord.nationalID = request.POST.get('regIDNo')
            saverecord.gender = request.POST.get('regGender')
            saverecord.address = request.POST.get('regAddress')
            try:
                saverecord.save()
            except IntegrityError as e:
                messages.error(request, "The email is already in use.")
                return render(request, 'records/policeOfficer.html')
            else:
                messages.success(request, 'Officer successfully registered.')
                return render(request, 'records/policeOfficer.html')
        else:
            messages.error(request, 'An error has occurred. Please contact an administrator.')
            return render(request, 'records/policeOfficer.html')
    else:
        return render(request, 'records/policeOfficer.html', {'title': 'Police Officer Register'})


def criminalBooking(request):
    if request.method == 'POST':
        if request.POST.get('criminalFName') and\
                request.POST.get('criminalLName') and\
                request.POST.get('criminalPhone') and\
                request.POST.get('criminalAddress') and\
                request.POST.get('criminalIDNo') and\
                request.POST.get('criminalGender') and\
                request.POST.get('crimeID') and\
                request.POST.get('criminalStatus') and\
                request.POST.get('arrestLocation') and\
                request.POST.get('arrestDate'):
            saverecord = Criminal()
            saverecord.fName = request.POST.get('criminalFName')
            saverecord.lName = request.POST.get('criminalLName')
            saverecord.tel = request.POST.get('criminalPhone')
            saverecord.address = request.POST.get('criminalAddress')
            saverecord.nationalID = request.POST.get('criminalIDNo')
            saverecord.gender = request.POST.get('criminalGender')
            saverecord.crimeID = request.POST.get('crimeID')
            saverecord.criminalStatus = request.POST.get('criminalStatus')
            saverecord.locationArrested = request.POST.get('arrestLocation')
            saverecord.arrestDate = request.POST.get('arrestDate')
            try:
                saverecord.save()
            except IntegrityError as e:
                messages.error(request, "Criminal email is already in the system.")
                return render(request, 'records/criminalBooking.html')
            else:
                messages.success(request, 'Criminal has been booked!')
                return render(request, 'records/criminalBooking.html')
        else:
            messages.error(request, 'An error has occurred. Please contact an administrator.')
            return render(request, 'records/criminalBooking.html')
    else:
        return render(request, 'records/criminalBooking.html', {'title': 'Criminal Booking'})


def evidence(request):
    return render(request, 'records/evidence.html', {'title': 'Evidence'})


def login(request):
    if request.method == "POST":
        if request.POST.get('loginEmail') and request.POST.get('loginPassword'):
            return render(request, 'records/login.html', {'title': 'Login'})
    else:
        return render(request, 'records/login.html', {'title': 'Login'})


def crimereport(request):
    if request.method == 'POST':
        if request.POST.get('description') and request.POST.get('crimeNature'):
            saverecord = Crime()
            saverecord.description = request.POST.get('description')
            saverecord.crimeNature = request.POST.get('crimeNature')
            try:
                saverecord.save()
            except Exception as e:
                messages.error(request, e)
                return render(request, 'records/crimereport.html')
            else:
                messages.success(request, 'Crime has been reported successfully!')
                return render(request, 'records/crimereport.html')
    else:
        return render(request, 'records/crimereport.html', {'title': 'Crime Report'})


def casetracking(request):
    return render(request, 'records/casetracking.html', {'title': 'Case Tracking '})

def casetransfer(request):
    return render(request, 'records/casetransfer.html', {'title': 'Case Transfer '})


def caseapproval(request):
    return render(request, 'records/caseapproval.html', {'title': 'Case Approval '})

def ob(request):
    return render(request, 'records/ob.html', {'title': 'OB '})

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
                request.POST.get('regGender') and\
                request.POST.get('regAddress'):
            # If the password and confirm password are same then the data will be saved in the database else an error message will be sent
            if request.POST.get('regPassword') == request.POST.get('regConPassword'):
                saverecord = Citizen()
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
                except IntegrityError as e:
                    messages.error(request, "The email entered is already in use.")
                    return render(request, 'records/signup.html')
                else:
                    messages.success(request, 'Record Saved Successfully...!')
                    return render(request, 'records/signup.html')
            else:
                # TODO add password not same error alert
                messages.error(request, 'Password does not match')
                return render(request, 'records/signup.html', {'title': 'Sign Up'})
    else:
        return render(request, 'records/signup.html', {'title': 'Sign Up'})


def dashboard(request):
    return render(request, 'records/dashboard.html', {'title': 'Dashboard'})


def landingpage(request):
    return render(request, 'records/landingpage.html', {'title': 'Landing Page', 'pageId': 8})
