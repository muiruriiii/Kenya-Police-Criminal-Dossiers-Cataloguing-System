import json
from datetime import datetime

from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from records.models import Officer as OfficerModel, Case as CaseModel, PoliceStation as PoliceStationModel, Crime as CrimeModel, Criminal as CriminalModel, Citizen as CitizenModel, CrimeList as CrimeListModel, OB as OBModel
from django.core.files.storage import FileSystemStorage


def PoliceStation(request):
    if request.method == "POST":
        if request.POST.get('statLocation') and request.POST.get('statAddress'):
            policeStation = PoliceStationModel(location=request.POST.get('statLocation'),
                                               address=request.POST.get('statAddress'),
                                               ocsID=request.session['officerID'])
            policeStation.save()
            stationID = policeStation.pk
            currentDate = datetime.now()
            stationNumber = '%s-%s-%s' % (stationID, policeStation.location, currentDate)
            policeStation.stationNumber = stationNumber
            policeStation.save()
            messages.success(request, 'Police Station has been added.')
            return render(request, 'PoliceOfficerApp/addStation.html', {'title': "Police Station", 'pageID':8})
    else:
        return render(request, 'PoliceOfficerApp/addStation.html', {'title': "Police Station"})


def ViewStations(request):
    station = PoliceStationModel.objects.all()
    return render(request, 'PoliceOfficerApp/viewStations.html', {'title': 'View Police Stations','stations':station})


def ShowStation(request, id):
    station = PoliceStationModel.objects.get(id=id)
    return render(request, 'PoliceOfficerApp/showStation.html', {'title': 'Show Station', 'station': station})


def CaseIndex(request):
    ob = OBModel.objects.filter(hasCase=0).all()
    cases = CaseModel.objects.all()
    return render(request, 'Case/index.html', {'title': 'Case', 'obs': ob, 'cases': cases})


def GenerateCase(request, id):
    case = CaseModel()
    case.officerID = request.session['officerID']
    case.obID = id
    case.caseStatus = 'PENDING'
    case.currentStation = request.session['officerStation']
    ob = OBModel.objects.get(id=id)

    try:
        case.save()
        currentDate = datetime.now()
        case.caseNumber = '%s-%s-%s' % ('CSF', case.pk, currentDate)
        case.save()
        ob.hasCase = case.pk
        ob.save()
    except Exception as e:
        messages.error(request, e)
        return redirect('PoliceOfficerApp:CaseIndex')
    else:
        messages.success(request, 'Case successfully generated.')
        return redirect('PoliceOfficerApp:CaseIndex')


def ApproveCase(request, id):
    return redirect('PoliceOfficerApp:CaseIndex')


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


def obDisplay(request, id):
    CrimesDisplay = CrimeModel.objects.get(id=id)
    if request.method == 'POST':
        if request.POST.get('obAction') and request.POST.get('citizenID') and request.POST.get('crimeID'):
            try:
                filepath = request.FILES['document']
            #This exception handles when there is no file uploaded
            except MultiValueDictKeyError:
                ob = OBModel(citizenID=request.POST.get('citizenID'),
                             crimeID=request.POST.get('crimeID'),
                             reportDate=request.POST.get('reportDate'),
                             actionTaken=request.POST.get('obAction'),
                             officerID=request.session['officerID'])
                try:
                    ob.save()
                    obID = ob.pk
                    obNumber = '%s/%s/%s' % (obID, datetime.now(), request.POST.get('citizenID'))
                    ob.obNo = obNumber
                    ob.file = None
                    ob.hasCase = 0
                    ob.save()
                    CrimesDisplay.hasOB = obID
                    CrimesDisplay.save()
                    messages.success(request, 'OB has been successfully generated')
                    return redirect('PoliceOfficerApp:CrimesDisplay')
                except Exception as e:
                    messages.error(request, e)
                    return redirect('PoliceOfficerApp:CrimesDisplay')
            else:
                fileStorage = FileSystemStorage()
                ob = OBModel(citizenID=request.POST.get('citizenID'),
                             crimeID=request.POST.get('crimeID'),
                             reportDate=request.POST.get('reportDate'),
                             actionTaken=request.POST.get('obAction'),
                             officerID=request.session['officerID'])
                ob.save()
                obID = ob.pk
                obNumber = '%s/%s/%s' % (obID, datetime.now(), request.POST.get('citizenID'))
                ob.obNo = obNumber
                ob.hasCase = 0
                ob.save()
                document = request.FILES.getlist('document')
                global documentsSet
                documentsSet = []
                documentCounter = 1
                for doc in document:
                    fileExtension= (doc.name).split(".",1)[1]
                    obFileName = 'ob-%s-%d.%s' % (obID, documentCounter, fileExtension)
                    documentCounter+=1
                    fileUrl = fileStorage.save('%s' % obFileName, doc)
                    uploadedFileName = ((fileStorage.url(fileUrl)).split("/", 2)[2])
                    documentsSet.append(uploadedFileName)
                ob.file = json.dumps(documentsSet)
                ob.save()
                #Change the crime record attribute 'hasOB' to True
                CrimesDisplay.hasOB = obID
                CrimesDisplay.save()
                messages.success(request, 'OB has been successfully generated')
                return redirect('PoliceOfficerApp:CrimesDisplay')
        else:
            messages.error(request, 'An error has been encountered. Contact the Administrator.')
            return render(request, 'PoliceOfficerApp/ob.html', {'CrimesDisplay': CrimesDisplay})
    else:
        return render(request, 'PoliceOfficerApp/ob.html', {'CrimesDisplay': CrimesDisplay})


def ViewOB(request, id):
    ob = OBModel.objects.get(id=id)
    obID = ob.pk
    citizenID = ob.citizenID
    crimeID = ob.crimeID
    obNo = ob.obNo
    actionTaken = ob.actionTaken
    global files
    files = []
    if ob.file is not None:
        for file in json.loads(ob.file):
            files.append(file)
    officerID = ob.officerID
    createDate = ob.createDate
    obDict = {'obID':obID,'citizenID': citizenID,'crimeID': crimeID,'obNo': obNo,'actionTaken': actionTaken,'officerID': officerID,'createDate': createDate,'files': files}
    return render(request, 'PoliceOfficerApp/viewOB.html',{'ob': obDict, 'title':'View OB'})


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
                    request.session['officerStation'] = officer.stationID
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


def index(request):
    if 'officerID' not in request.session:
        return redirect('PoliceOfficerApp:OfficerLogin')
    else:
        return render(request, 'PoliceOfficerApp/index.html', {'title': 'Police Dashboard', 'pageID': 1})


def OfficersDisplay(request):
    if 'officerID' not in request.session:
        return redirect('PoliceOfficerApp:OfficerLogin')
    else:
        officers = OfficerModel.objects.all()
        context = {'officers': officers, 'pageID': 2, 'title': 'List of Officers'}
        return render(request, 'PoliceOfficerApp/OfficersDisplay.html', context)


def CitizensDisplay(request):
    if 'officerID' not in request.session:
        return redirect('PoliceOfficerApp:OfficerLogin')
    else:
        citizens = CitizenModel.objects.all()
        context = {'citizens': citizens, 'pageID': 3, 'title': 'Citizen Display'}
        return render(request, 'PoliceOfficerApp/CitizensDisplay.html', context)


def CriminalsDisplay(request):
    if 'officerID' not in request.session:
        return redirect('PoliceOfficerApp:OfficerLogin')
    else:
        criminals = CriminalModel.objects.all()
        context = {'criminals': criminals, 'pageID': 4, 'title': 'Criminals Display'}
        return render(request, 'PoliceOfficerApp/CriminalsDisplay.html', context)


def CrimeListDisplay(request):
    if 'officerID' not in request.session:
        return redirect('PoliceOfficerApp:OfficerLogin')
    else:
        crimelist = CrimeListModel.objects.all()
        context = {'crimelist': crimelist, 'pageID': 5, 'title': 'Crime List Display'}
        return render(request, 'PoliceOfficerApp/CrimeListDisplay.html', context)


def CrimesDisplay(request):
    if 'officerID' not in request.session:
        return redirect('PoliceOfficerApp:OfficerLogin')
    else:
        crimes = CrimeModel.objects.all()
        global crime_list
        crime_list=[]
        for crime in crimes:
            citizenID = crime.citizenID
            citizens = CitizenModel.objects.get(id=citizenID)
            citizenName = citizens.fName+' '+citizens.lName

            crimeID = crime.crimeID
            crimelist = CrimeListModel.objects.get(crimeID=crimeID)
            crimeName = crimelist.crimeName
            crimesreported={'id': crime.pk, 'description': crime.description, 'citizenName': citizenName, 'crimeName': crimeName, 'obNumber': crime.hasOB}
            crime_list.append(crimesreported)
            #crimeReportID,crimeDescription, crimeName, citizenName
        context = {'crimesreported': crime_list, 'pageID': 6, 'title': 'Crime Display'}
        return render(request, 'PoliceOfficerApp/CrimesDisplay.html', context)


def OfficerProfile(request):
    if 'officerID' not in request.session:
        return redirect('PoliceOfficerApp:OfficerLogin')
    else:
        officer = OfficerModel.objects.get(id=request.session['officerID'])
        context = {'officer': officer, 'pageID': 7, 'title': 'Officer Profile'}
        return render(request, 'PoliceOfficerApp/OfficerProfile.html', context)
