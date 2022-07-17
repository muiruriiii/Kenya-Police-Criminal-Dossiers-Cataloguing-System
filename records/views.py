from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
from django.shortcuts import redirect
from records.models import Citizen as CitizenModel, CrimeList as CrimeListModel, Crime as CrimeModel, \
    CrimeAnonymous as CrimeAnonymousModel, Evidence as EvidenceModel
from django.shortcuts import render



def evidence(request):
    context = {}
    if request.method == 'POST':
       if  request.FILES['evidenceFiles'] and request.FILES['Form']  and request.POST.get('description') :

           fileStorage = FileSystemStorage()
           evidenceFiles = request.FILES['evidenceFiles']
           Form = request.FILES['Form']
           saverecord = EvidenceModel()
           saverecord.description = request.POST.get('description')


           try:
               saverecord.save()
               id = saverecord.pk
               name = 'evidence-%s%s' % (id, '.jpg')
               name2 = 'form-%s%s' % (id, '.pdf')

               display = fileStorage.save('%s' % name, evidenceFiles)
               context['url']=fileStorage.url(display)


               saverecord.evidenceFiles = name
               saverecord.Form = name2
               saverecord.save()
           except IntegrityError as e:
               messages.error(request, e)
               return render(request, 'records/evidence.html',context)
           else:
               messages.success(request, 'Evidence Uploaded Successfully...!')
               return render(request, 'records/evidence.html', context)
       else:
           messages.error(request, 'Upload Not Successful...')
           return render(request, 'records/evidence.html',context)
    else:
           return render(request, 'records/evidence.html', context)


def CrimeListDisplay(request):
    crimelist = CrimeListModel.objects.all()
    if request.method == 'POST':
        if request.POST.get('crimeID') and request.POST.get('crimeDescription'):
            # Here we check if a citizen is logged in so that we can decide whether the crime has been reported anonymously or not.
            if 'citizenID' in request.session:
                if request.POST.get('anonymous'):
                    crimeAnonymous = CrimeAnonymousModel()
                    crimeAnonymous.crimeID = CrimeListModel.objects.get(crimeID=request.POST.get('crimeID')).pk
                    crimeAnonymous.description = request.POST.get('crimeDescription')
                    try:
                        crimeAnonymous.save()
                    except Exception as e:
                        messages.error(request, e)
                        return render(request, "records/crimereport.html", {"crimelists": crimelist})
                    else:
                        messages.success(request, 'Crime has been reported successfully!')
                        return render(request, "records/crimereport.html", {"crimelists": crimelist})
                else:
                    print(request.FILES.getlist('crimeFiles'))
                    crime = CrimeModel()
                    crime.crimeID = CrimeListModel.objects.get(crimeID=request.POST.get('crimeID')).pk
                    crime.description = request.POST.get('crimeDescription')
                    crime.citizenID = request.session['citizenID']
                    try:
                        crime.save()
                    except Exception as e:
                        messages.error(request, e)
                        return render(request, "records/crimereport.html", {"crimelists": crimelist})
                    else:
                        messages.success(request, 'Crime has been reported successfully!')
                        return render(request, "records/crimereport.html", {"crimelists": crimelist})
            else:
                crimeAnonymous = CrimeAnonymousModel()
                crimeAnonymous.crimeID = CrimeListModel.objects.get(crimeID=request.POST.get('crimeID')).pk
                crimeAnonymous.description = request.POST.get('crimeDescription')
                try:
                    crimeAnonymous.save()
                except Exception as e:
                    messages.error(request, e)
                    return render(request, "records/crimereport.html", {"crimelists": crimelist})
                else:
                    messages.success(request, 'Crime has been reported successfully!')
                    return render(request, "records/crimereport.html", {"crimelists": crimelist})
        else:
            messages.error(request, 'An error has occurred')
            return render(request, "records/crimereport.html", {"crimelists": crimelist})
    else:
        return render(request, "records/crimereport.html", {"crimelists": crimelist})


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
        if request.POST.get('regFName') and \
                request.POST.get('regLName') and \
                request.POST.get('regEmail') and \
                request.POST.get('regPhone') and \
                request.POST.get('regPassword') and \
                request.POST.get('regConPassword') and \
                request.POST.get('regIDNo') and \
                request.POST.get('regGender') and \
                request.FILES['citizenImage'] and \
                request.POST.get('regAddress'):
            # If the password and confirm password are same then the data will be saved in the database else an error message will be sent
            if request.POST.get('regPassword') == request.POST.get('regConPassword'):
                # Getting the image that has been uploaded
                fileStorage = FileSystemStorage()
                citizenImage = request.FILES['citizenImage']

                saverecord = CitizenModel()
                saverecord.fName = request.POST.get('regFName')
                saverecord.lName = request.POST.get('regLName')
                saverecord.email = request.POST.get('regEmail')
                saverecord.tel = request.POST.get('regPhone')

                # Hash password before recording in the DB
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

