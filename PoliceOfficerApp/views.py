from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .forms import EditForm
from records.models import Officer as OfficerModel, Crime as CrimeModel, Criminal as CriminalModel, Citizen as CitizenModel, CrimeList as CrimeListModel
from django.core.files.storage import FileSystemStorage



# def upload(request):
#     context = {}
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)
#     return render(request,'PoliceOfficerApp/upload.html',context)

def ob(request):
    return render(request, 'PoliceOfficerApp/ob.html', {'title': 'OB  '})
# display list of crimes
# def CrimeListsDisplay(request):
#     crimelistdisplay = CrimeListModel.objects.all()
#     return render(request, "PoliceOfficerApp/ob.html")


def addCrimes(request):
    if request.method == 'POST':
        if request.POST.get('crimeName'):
            saverecord = CrimeListModel()
            saverecord.crimeName = request.POST.get('crimeName')
            try:
                saverecord.save()
            except Exception as e:
                messages.error(request, e)
                return render(request, 'PoliceOfficerApp/addCrimes.html')
            else:
                messages.success(request, 'Crime has been added successfully!')
                return render(request, 'PoliceOfficerApp/addCrimes.html')
    else:
        return render(request, 'PoliceOfficerApp/addCrimes.html', {'title': 'Crime Report'})

def ob(request):
    # if request.method == 'POST':
    #     if request.POST.get('file'):
    #         saverecord = OB()
    #         saverecord.file = request.POST.get('file')
    #         try:
    #             saverecord.save()
    #         except Exception as e:
    #             messages.error(request, e)
    #             return render(request, 'PoliceOfficerApp/addCrimes.html')
    #         else:
    #             messages.success(request, 'Crime has been added successfully!')
    #             return render(request, 'PoliceOfficerApp/addCrimes.html')
    # else:
        return render(request, 'PoliceOfficerApp/ob.html', {'title': 'Crime Report'})


# calls the EditCriminal page and the details of the row you want to CriminalEdit are prefilled
def CriminalEdit(request, id):
    CriminalsDisplay = CriminalModel.objects.get(id=id)
    if request.method == 'POST':
        if request.POST.get('criminalFName') and \
                request.POST.get('criminalLName') and \
                request.POST.get('criminalPhone') and \
                request.POST.get('criminalAddress') and \
                request.POST.get('criminalIDNo') and \
                request.POST.get('criminalGender') and \
                request.POST.get('crimeID') and \
                request.POST.get('criminalStatus') and \
                request.POST.get('arrestLocation') and \
                request.POST.get('arrestDate'):
            CriminalsDisplay.fName = request.POST.get('criminalFName')
            CriminalsDisplay.lName = request.POST.get('criminalLName')
            CriminalsDisplay.tel = request.POST.get('criminalPhone')
            CriminalsDisplay.address = request.POST.get('criminalAddress')
            CriminalsDisplay.nationalID = request.POST.get('criminalIDNo')
            CriminalsDisplay.gender = request.POST.get('criminalGender')
            CriminalsDisplay.crimeID = request.POST.get('crimeID')
            CriminalsDisplay.criminalStatus = request.POST.get('criminalStatus')
            CriminalsDisplay.locationArrested = request.POST.get('arrestLocation')
            CriminalsDisplay.arrestDate = request.POST.get('arrestDate')
            try:
                CriminalsDisplay.save()
            except Exception as e:
                messages.error(request, e)
                return render(request, 'PoliceOfficerApp/EditCriminal.html')
            else:
                messages.success(request, 'Criminal has been updated!')
                return redirect('PoliceOfficerApp:CriminalsDisplay')
        else:
            return render(request, 'PoliceOfficerApp/EditCriminal.html', {'CriminalsDisplay': CriminalsDisplay})
    else:
        return render(request, 'PoliceOfficerApp/EditCriminal.html', {'CriminalsDisplay': CriminalsDisplay})


def OfficerEdit(request, id):
    officer = OfficerModel.objects.get(id=id)
    if request.method == 'POST':
        if request.POST.get('regEmail') and \
                request.POST.get('regPhone') and \
                request.POST.get('regGender') and \
                request.POST.get('regAddress'):
            officer.email = request.POST.get('regEmail')
            officer.tel = request.POST.get('regPhone')
            officer.gender = request.POST.get('regGender')
            officer.address = request.POST.get('regAddress')
            try:
                officer.save()
            except Exception as e:
                messages.error(request, e)
                return render(request, 'PoliceOfficerApp/OfficerRegister.html')
            else:
                messages.success(request, 'Officer details successfully updated.')
                return redirect('PoliceOfficerApp:OfficerProfile')
        # else:
        #     messages.error(request, 'An error has occurred. Please contact an administrator.')
        #     return render(request, 'PoliceOfficerApp/EditOfficer.html', {'title': 'Officer Edit', 'officer': officer})
    else:
        return render(request, 'PoliceOfficerApp/EditOfficer.html', {'title': 'Officer Edit', 'officer': officer})


def OfficerRegister(request):
    if request.method == 'POST':
        if request.POST.get('regFName') and \
                request.POST.get('regLName') and \
                request.POST.get('regEmail') and \
                request.POST.get('regPhone') and \
                request.POST.get('regRank') and \
                request.POST.get('regIDNo') and \
                request.POST.get('regGender') and \
                request.POST.get('regAddress'):
            saverecord = OfficerModel()
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
                return render(request, 'PoliceOfficerApp/OfficerRegister.html')
            else:
                messages.success(request, 'Officer successfully registered.')
                return render(request, 'PoliceOfficerApp/OfficerRegister.html')
        else:
            messages.error(request, 'An error has occurred. Please contact an administrator.')
            return render(request, 'PoliceOfficerApp/OfficerRegister.html')
    else:
        return render(request, 'PoliceOfficerApp/OfficerRegister.html', {'title': 'Police Officer Register'})

def criminalbooking(request):
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
            saverecord = CriminalModel()
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
                return render(request, 'PoliceOfficerApp/criminalbooking.html')
            else:
                messages.success(request, 'Criminal has been booked!')
                return render(request, 'PoliceOfficerApp/criminalbooking.html')
        else:
            messages.error(request, 'An error has occurred. Please contact an administrator.')
            return render(request, 'PoliceOfficerApp/criminalbooking.html')
    else:
        return render(request, 'PoliceOfficerApp/criminalbooking.html', {'title': 'Criminal Booking'})


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

