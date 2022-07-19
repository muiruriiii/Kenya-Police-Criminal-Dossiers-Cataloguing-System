from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from records.views import landingpage
from records.models import Citizen as CitizenModel


def CitizenProfile(request):
    if 'citizenID' in request.session:
        citizen = CitizenModel.objects.get(id=request.session['citizenID'])
        return render(request, 'CitizenApp/citizenProfile.html', {'citizen': citizen})
    else:
        return redirect('CitizenApp:CitizenLogin')


def CitizenLogin(request):
    if request.method == "POST":
        if request.POST.get('loginEmail') and request.POST.get('loginPassword'):
            loginEmail = request.POST.get('loginEmail')
            loginPassword = request.POST.get('loginPassword')
            citizen = CitizenModel.objects.get(email=loginEmail)

            if check_password(loginPassword, citizen.password):
                # TODO create single variable that stores individual column of the citizen table.
                request.session['citizenID'] = citizen.id
                request.session['citizenName'] = citizen.fName + ' ' + citizen.lName
                request.session['citizenImage'] = citizen.citizenImage.url

                # currentCitizen = CitizenClass(citizen.id,citizen.fName,citizen.lName,citizen.email,citizen.tel,citizen.password,citizen.nationalID,citizen.gender,citizen.address)

                # return render(request, 'records/CitizenLogin.html')
                return redirect(landingpage)
            else:
                messages.error(request, 'Invalid Password.Please Try Again...')
                return render(request, 'records/CitizenLogin.html', {'title': 'Login'})
    else:
        return render(request, 'records/CitizenLogin.html', {'title': 'Login'})


def CitizenLogout(request):
    try:
        del request.session['citizenID']
    except Exception as e:
        messages.error(request, e)
    else:
        messages.success(request, 'Logged out.')
        return redirect('/', {'title': 'Landing Page', 'pageId': 8})


def CitizenEdit(request, id):
    if 'citizenID' in request.session:
        citizen = CitizenModel.objects.get(id=id)
        if request.method == 'POST':
            if request.POST.get('regEmail') and \
                    request.POST.get('regPhone') and \
                    request.POST.get('regAddress'):
                citizen.email = request.POST.get('regEmail')
                citizen.tel = request.POST.get('regPhone')
                citizen.address = request.POST.get('regAddress')

                try:
                    citizenImage = request.FILES['citizenImage']
                except MultiValueDictKeyError as e:
                    citizen.save()
                    return redirect('CitizenApp:CitizenProfile')
                except Exception as e:
                    messages.error(request, e)
                    return render(request, 'CitizenApp/EditCitizen.html')
                else:
                    fileStorage = FileSystemStorage()
                    citizenImageName = 'citizen-%s%s' % (citizen.id, '.jpg')
                    fileStorage.save('%s' % citizenImageName, citizenImage)
                    citizen.citizenImage = fileStorage.save('%s' % citizenImageName, citizenImage)
                    citizen.save()
                    request.session['citizenImage'] = citizen.citizenImage.url
                    messages.success(request, 'citizen details successfully updated.')
                    return redirect('CitizenApp:CitizenProfile')
            else:
                messages.error(request, 'An error has occurred. Please contact an administrator.')
                return render(request, 'CitizenApp/EditCitizen.html', {'title': 'citizen Edit', 'citizen': citizen})
        else:
            return render(request, 'CitizenApp/EditCitizen.html', {'title': 'Citizen Edit', 'citizen': citizen})
    else:
        return redirect('CitizenApp:CitizenLogin')
