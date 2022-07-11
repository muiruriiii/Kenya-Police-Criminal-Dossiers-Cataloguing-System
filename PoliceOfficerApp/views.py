from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .forms import EditForm
from records.models import Officer as OfficerModel, Crime as CrimeModel, Criminal as CriminalModel, Citizen as CitizenModel


def ob(request):
    return render(request, 'PoliceOfficerApp/ob.html', {'title': 'OB  '})

# calls the EditCriminal page and the details of the row you want to edit are prefilled
def edit(request, id):
  CriminalsDisplay = CriminalModel.objects.get(id=id)
  return render(request, 'PoliceOfficerApp/EditCriminal.html',{'CriminalsDisplay': CriminalsDisplay})

# to save the updated data
def update(request, id):
    criminal = CriminalModel.objects.get(id=id)
    form = EditForm(request.POST or None, instance=criminal)
# validate the form then save the data and redirect the page
    if form.is_valid():
        form.save()
        messages.success(request, 'The criminal was updated successfully...')
        return redirect('PoliceOfficerApp:CriminalsDisplay')
    else:
        messages.error(request, "The criminal was not updated successfully...")
        return render(request, 'PoliceOfficerApp/EditCriminal.html', {'form': form})


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
                return render(request, 'records/criminalbooking.html')
            else:
                messages.success(request, 'Criminal has been booked!')
                return render(request, 'records/criminalbooking.html')
        else:
            messages.error(request, 'An error has occurred. Please contact an administrator.')
            return render(request, 'records/criminalbooking.html')
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

