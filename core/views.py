from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from .models import Video
from .models import Contact
from .models import Dealer
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def contactus(request):
    if request.method == 'POST':
        dealer=Dealer()
        user = request.POST.get('username')
        email = request.POST.get('email')
        ph_number = request.POST.get('contact')
        message = request.POST.get('message')

        dealer.user=user
        dealer.email=email
        dealer.ph_number=ph_number
        dealer.message=message
        dealer.save()
        if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/contactus')
    return HttpResponse("THANKS FOR CONTACT")            
    return render(request, 'contactus.html')
def option(request):
    return render(request, 'option.html')
def about(request):
    return render(request, 'aboutus.html')
def main(request):
   
    if request.method == 'POST':

     contact=Contact()
     user = request.POST.get('username')
     email = request.POST.get('email')
     subject = request.POST.get('about')


     contact.user=user
     contact.email=email
     contact.subject=subject
     
     contact.save()
     if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/main')
     return HttpResponse("THANKS FOR CONTACT")
     
    
    return render(request, 'main.html')

      
def indes(request):
   
    return render(request, 'index-1.html')
@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')
@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':

        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        if request.FILES.get('image') != None:

            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()

        return redirect('settings')

    return render(request, 'setting.html')
def signup(request):

    if request.method == 'POST':

        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #Log user in and redirect to setting page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a profile
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signin')
        else:
            messages.info(request, 'Password Dont match')
            return redirect('signup')


    else:
        return render(request, 'signup.html')



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/main')
        else:
            messages.info(request,'You need to create an account ASAP!!!')
            return redirect('/signin')
    else:
        return render(request, 'signin.html')

@login_required(login_url='signin')
def Logout(request):
    auth.logout(request)
    return redirect('signin')

