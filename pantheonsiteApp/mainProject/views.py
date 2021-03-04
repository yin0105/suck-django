from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import ExtendedUserCreationForm, UserInformationForm
from .models import UserInformations
# Create your views here.

def home(request):
    return render(request, 'home.html')

def fortySolutions(request):
    context = {}
    template = 'companies/48forty-solutions.html'
    return render(request, template, context)

def earthFarms(request):
    context = {}
    template = 'companies/4earth-Farms.html'
    return render(request, template, context)

def organicFarms(request):
    context = {}
    template = 'companies/organic-Farms.html'
    return render(request, template, context)

def coldStorage(request):
    context = {}
    template = 'companies/cold-Storage.html'
    return render(request, template, context)

def thomasProduce(request):
    context = {}
    template = 'companies/thomas-Produce.html'
    return render(request, template, context)

def abbottCobb(request):
    context = {}
    template = 'companies/abbott-Cobb.html'
    return render(request, template, context)

def abcResearchLabs(request):
    context = {}
    template = 'companies/abc-Research-Labs.html'
    return render(request, template, context)

def abl(request):
    context = {}
    template = 'companies/abl.html'
    return render(request, template, context)

def amerifresh(request):
    context = {}
    template = 'companies/amerifresh.html'
    return render(request, template, context)

def amhpac(request):
    context = {}
    template = 'companies/amhpac.html'
    return render(request, template, context)

def ampco(request):
    context = {}
    template = 'companies/ampco.html'
    return render(request, template, context)

def amrAgro(request):
    context = {}
    template = 'companies/amr-Agro.html'
    return render(request, template, context)

def manage(request):
    return render(request, 'manage.html')

def logout_attempt(request):
    logout(request)
    return redirect('/')


def login_attempt(request):
    print(request.get_host())
    if request.method == 'POST':
        print('----- this is the login -----')
        email = request.POST['email']
        password = request.POST['password']
        image_user = User.objects.filter(email=email).first()
        if image_user:
            user = authenticate(request, username=image_user.username, password = password)
            print(user)
            if user is not None:
                login(request, user)
                print("--- logged in ----")
                return redirect('admin/profile')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        template = 'auth/login.html'
        return render(request, template)

def social_auth(request):
    if request.method == "POST":
        social_type = request.POST['social_type']
        social_provide_id = request.POST['social_id']
        social_email = request.POST['social_email']
        social_image = request.POST['social_image']
        social_name = request.POST['social_name']
        if social_type == 'google':
           user_information = UserInformations.objects.filter(google_auth_verify=True, google_auth_provide_id=social_provide_id).first()
        elif social_type == 'linkedin':
            user_information = UserInformations.objects.filter(linkedin_auth_verify=True, linkedin_auth_provide_id=social_provide_id).first()
        else:
          user_information = UserInformations.objects.filter(outlook_auth_verify=True, outlook_auth_provide_id=social_provide_id).first()
        if user_information is not None:
            user = authenticate(request, username=user_information.user.username, password = user_information.real_password)
            login(request, user)
            return JsonResponse({'status': 1, 'data':'result'})
        else:
            return JsonResponse({'status': 0, 'data':'result'})
    else:
        return JsonResponse({'status': 0, 'data':'result'})
        


def register_attempt(request):
    context = {}
    if request.method == 'POST':
        print('----- register -----')
        form = ExtendedUserCreationForm(request.POST)
        information_form = UserInformationForm(request.POST)
        email = request.POST['email']
        print("1")
        if form.is_valid() and information_form.is_valid():
            print("valid")
            username = request.POST['username']
            password = request.POST['password1']

            user = form.save()
            information = information_form.save(commit= False)
            information.user = user
            information.email_token = get_random_string(length=32)
            information.real_password = request.POST['password1']
            information.save()

            #  print(username)
            # print(password)

            # user = authenticate(request, username=username, password = password)
            # print(user)

            url = 'http://localhost:8000/'
            # url = 'http://' + request.get_host() + '/'
            # url = 'http://v8.andnowuknow.com/'
            content = "Please click this follow link to confirm: " + url + 'email-verify?token=' + information.email_token
            try:
                send_mail('Welcome to AndNowYouKnow.', content , 'from@email.com', [email], fail_silently=False)
                return redirect('check-email')
            except: 
                context['error'] = "Invalid email."
                return redirect('register')
    else:
        form = ExtendedUserCreationForm()
        information_form = UserInformationForm()
    context = {'form' : form, 'information_form': information_form}    
    template = 'auth/register.html'
    return render(request, template, context)

def check_email(request):
    return render(request, 'auth/check_email.html')

def email_verify(request):
    token = request.GET["token"]
    profile = UserInformations.objects.filter(email_token=token).first()
    if profile:
        print("------ this is the user information ------")
        User.objects.filter(id=profile.user_id).update(is_active=True)
        UserInformations.objects.filter(email_token=token).update(email_verify=True)
        user = authenticate(request, username=profile.user.username, password = profile.real_password)
        print(user)
        login(request, user)
        return admin_profile(request)
    else:
        return redirect('login')

@login_required
def admin_profile(request):
    user_information = UserInformations.objects.filter(user_id=request.user.id).first()
    context = { 'user_information': user_information }
    return render(request, 'admin/users/profile.html', context)

@login_required
def admin_profile_update(request):
    if request.method == 'POST':
        social_type = request.POST['social_type']
        social_provide_id = request.POST['social_id']
        social_email = request.POST['social_email']
        social_image = request.POST['social_image']
        social_name = request.POST['social_name']
        if social_type == 'google':
            UserInformations.objects.filter(user_id=request.user.id).update(google_auth_verify=True, google_auth_email=social_email, google_auth_image=social_image, google_auth_name=social_name, google_auth_provide_id=social_provide_id)
        if social_type == 'linkedin':
            UserInformations.objects.filter(user_id=request.user.id).update(linkedin_auth_verify=True, linkedin_auth_email=social_email, linkedin_auth_image=social_image, linkedin_auth_name=social_name, linkedin_auth_provide_id=social_provide_id)
        if social_type == 'outlook':
            UserInformations.objects.filter(user_id=request.user.id).update(outlook_auth_verify=True, outlook_auth_email=social_email, outlook_auth_image=social_image, outlook_auth_name=social_name, outlook_auth_provide_id=social_provide_id)
        return JsonResponse({'status': 1, 'data':'result'})
    else:
        return JsonResponse({'status': 0, 'data':'result'})

