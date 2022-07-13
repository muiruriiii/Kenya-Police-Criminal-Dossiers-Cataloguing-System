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

from records.models import Citizen as CitizenModel
from records.models import Crime
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from police_system.helpers.tokens import *


def evidence(request):
    return render(request, 'records/evidence.html', {'title': 'Evidence'})


def crimereport(request):
    if request.method == 'POST':
        if request.POST.get('crimeDescription') and request.POST.get('crimeNature') and request.POST.get('voice_record'):
            saverecord = Crime()
            saverecord.description = request.POST.get('crimeDescription')
            saverecord.crimeNature = request.POST.get('crimeNature')
            saverecord.voice_record = request.POST.get('voice_record')
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
                    fileStorage.save(citizenImageName, citizenImage)
                    saverecord.citizenImage = citizenImageName
                    saverecord.save()
                    # current_site = get_current_site(request)
                    # mail_subject = 'Activate your account.'
                    # message = render_to_string('records/email_template.html', {
                    #     'user': saverecord,
                    #     'domain': current_site.domain,
                    #     'uid': urlsafe_base64_encode(force_bytes(citizenID)),
                    #     'token': account_activation_token.make_token(saverecord),
                    # })
                    # to_email = request.POST.get('regEmail')
                    # send_mail(mail_subject, message, 'muiruricynthiaaa@gmail.com', [to_email])
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


# def activate(request, uidb64, token):
#     citizen = CitizenModel
#     try:
#         uid = force_bytes(urlsafe_base64_decode(uidb64))
#         user = citizen.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, citizen.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')


def dashboard(request):
    return render(request, 'records/dashboard.html', {'title': 'Dashboard'})


def landingpage(request):
    return render(request, 'records/index.html', {'title': 'Landing Page', 'pageId': 8})
