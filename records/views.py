from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect, HttpResponse
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
            return redirect('dashboard')
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
            saverecord.password = make_password(request.POST.get('password'))
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

# to select crime information(not complete)
def crime(request):
    form = CrimeInsert.objects.all()
    context = {'form': form}
    return render(request, 'records/crime.html',context)

# check password
def login(request):
    if request.method == 'POST':
        request.POST['email']
        encryptedpassword=make_password(request.POST['password'])
        print(encryptedpassword)
        checkpassword=check_password(request.POST['password'], encryptedpassword)

        return redirect('landingpage')
    else:
        return redirect('login')

        return render(request, 'records/login.html', {'title': 'Sign Up'})

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
                saverecord = InsertUser()
                saverecord.fName = request.POST.get('regFName')
                saverecord.lName = request.POST.get('regLName')
                saverecord.email = request.POST.get('regEmail')
                saverecord.tel = request.POST.get('regPhone')

                #Hash password before recording in the DB
                saverecord.password = make_password(request.POST.get('regPassword'))
                saverecord.nationalID = request.POST.get('regIDNo')
                saverecord.gender = request.POST.get('regGender')
                saverecord.address = request.POST.get('regAddress')
                saverecord.save()
                messages.success(request, 'Record Saved Successfully...!')
                return redirect('login')
            else:
                # TODO add password not same error alert
                messages.error(request, 'Password does not match')
                return redirect('signup')
    else:
        return render(request, 'records/signup.html', {'title': 'Sign Up'})




def crimereport(request):
    if request.method == 'POST':
        if request.POST.get('description') and request.POST.get('crimeNature'):
            saverecord = CrimeInsert()
            saverecord.description = request.POST.get('description')
            saverecord.crimeNature = request.POST.get('crimeNature')
            saverecord.save()
            messages.success(request, 'Record Saved Successfully...!')
            return render(request, 'records/landingpage.html')
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

def dashboard(request):
    return render(request, 'records/dashboard.html', {'title': 'Dashboard'})


def landingpage(request):
    return render(request, 'records/landingpage.html', {'title': 'Landing Page', 'pageId': 8})


