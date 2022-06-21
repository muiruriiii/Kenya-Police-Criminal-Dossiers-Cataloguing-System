from django.shortcuts import render, redirect
from django.contrib import messages
from records.models import CrimeInsert
from records.models import InsertUser
from records.models import InsertCriminal
from records.models import InsertOfficer

def policeofficer(request):
    if request.method == 'POST':
        if request.POST.get('fName') and request.POST.get('lName') and request.POST.get('email') and request.POST.get('tel')  and request.POST.get('nationalID') and request.POST.get('gender') and request.POST.get(
                'DOB')  and request.POST.get(
                'rank') and request.POST.get('password') and request.POST.get(
                'employmentStatus') and request.POST.get('employmentDate'):
            saverecord = InsertOfficer()
            saverecord.fName = request.POST.get('fName')
            saverecord.lName = request.POST.get('lName')
            saverecord.email = request.POST.get('email')
            saverecord.tel = request.POST.get('tel')
            saverecord.nationalID = request.POST.get('nationalID')
            saverecord.gender = request.POST.get('gender')
            saverecord.DOB = request.POST.get('DOB')
            saverecord.rank = request.POST.get('rank')
            saverecord.password = request.POST.get('password')
            saverecord.employmentStatus = request.POST.get('employmentStatus')
            saverecord.employmentDate = request.POST.get('employmentDate')
            saverecord.save()
            messages.success(request, 'Record Saved Successfully...!')
            return render(request, 'records/policeofficer.html')
    else:
        return render(request, 'records/policeofficer.html', {'title': 'Police Officer'})


def criminalbooking(request):
    if request.method == 'POST':
        if request.POST.get('fName') and request.POST.get('lName') and request.POST.get('tel') and request.POST.get('address') and request.POST.get('nationalID') and request.POST.get( 'gender') and request.POST.get('crimeID') and request.POST.get('criminalStatus') and request.POST.get('locationArrested') and request.POST.get('arrestDate'):
            saverecord = InsertCriminal()
            saverecord.fName = request.POST.get('fName')
            saverecord.lName = request.POST.get('lName')
            saverecord.tel = request.POST.get('tel')
            saverecord.address = request.POST.get('address')
            saverecord.nationalID = request.POST.get('nationalID')
            saverecord.gender = request.POST.get('gender')
            saverecord.crimeID = request.POST.get('crimeID')
            saverecord.criminalStatus = request.POST.get('criminalStatus')
            saverecord.locationArrested = request.POST.get('locationArrested')
            saverecord.arrestDate = request.POST.get('arrestDate')
            saverecord.save()
            messages.success(request, 'Record Saved Successfully...!')
            return render(request, 'records/criminalbooking.html')
    else:
        return render(request, 'records/criminalbooking.html', {'title': 'Criminal Booking'})


def evidence(request):
    return render(request, 'records/evidence.html', {'title': 'Evidence'})


def login(request):
    return render(request, 'records/login.html', {'title': 'Login'})


def crimereport(request):
    if request.method == 'POST':
        if request.POST.get('description') and request.POST.get('crimeNature'):
            saverecord = CrimeInsert()
            saverecord.description = request.POST.get('description')
            saverecord.crimeNature = request.POST.get('crimeNature')
            saverecord.save()
            messages.success(request, 'Record Saved Successfully...!')
            return render(request, 'records/crimereport.html')
    else:
        return render(request, 'records/crimereport.html', {'title': 'Crime Report'})


def casetracking(request):
    return render(request, 'records/casetracking.html', {'title': 'Case Tracking '})


def ob(request):
    return render(request, 'records/ob.html', {'title': 'OB '})


def signup(request):
    if request.method == 'POST':
        if request.POST.get('fName') and request.POST.get('lName') and request.POST.get('email') and request.POST.get(
                'tel') and request.POST.get('password') and request.POST.get('nationalID') and request.POST.get(
                'gender') and request.POST.get('address'):
            saverecord = InsertUser()
            saverecord.fName = request.POST.get('fName')
            saverecord.lName = request.POST.get('lName')
            saverecord.email = request.POST.get('email')
            saverecord.tel = request.POST.get('tel')
            saverecord.password = request.POST.get('password')
            saverecord.nationalID = request.POST.get('nationalID')
            saverecord.gender = request.POST.get('gender')
            saverecord.address = request.POST.get('address')
            saverecord.save()
            messages.success(request, 'Record Saved Successfully...!')
            return render(request, 'records/signup.html')
    else:
        return render(request, 'records/signup.html', {'title': 'Sign Up'})


def dashboard(request):
    return render(request, 'records/dashboard.html', {'title': 'Dashboard'})


def landingpage(request):
    return render(request, 'records/landingpage.html', {'title': 'Landing Page', 'pageId': 8})
