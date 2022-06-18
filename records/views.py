from django.shortcuts import render, redirect
from django.contrib import messages



def policeofficer(request):
    return render(request, 'records/policeofficer.html',{'title':'Police Officer'})

def criminalbooking(request):
    return render(request, 'records/criminalbooking.html',{'title':'Criminal Booking'})

def evidence(request):
    return render(request, 'records/evidence.html',{'title':'Evidence'})

def login(request):
    return render(request, 'records/login.html',{'title':'Login'})

def crimereport(request):
    return render(request, 'records/crimereport.html',{'title':'Crime Report'})

def casetracking(request):
    return render(request, 'records/casetracking.html',{'title':'Case Tracking '})

def ob(request):
    return render(request, 'records/ob.html',{'title':'OB '})

def signup(request):
    return render(request, 'records/signup.html',{'title':'Sign Up '})

def dashboard(request):
    return render(request, 'records/dashboard.html',{'title':'Dashboard'})

def landingpage(request):
    return render(request, 'records/landingpage.html', {'title':'Landing Page', 'pageId': 8})
