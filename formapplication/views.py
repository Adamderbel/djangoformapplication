from django.shortcuts import render , redirect
from .models import Profile
from .forms import SingupForm , UserForm ,ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
def singup (request):
    if request.method == 'POST':
        form= SingupForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            email = form.cleaned_data['email']
            messages.success(request, f'Hi {username}, A confirmation email has been sent to you ')
            send_confirmation_email(request,email)
    else:
        form=SingupForm()
    return render(request,'registration/singup.html',{'form':form})
def send_confirmation_email(request,email):
    subject = 'Confirmation Email'
    message = 'Thank you for registering. Please click the link below to log in.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    login_url = reverse('login') 
    email_message = f"{message}\n\nLogin URL: {request.build_absolute_uri(login_url)}"
    send_mail(subject, email_message, from_email, recipient_list)

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'profile/profile.html',{'profile':profile})


      
@login_required
def profile_edit(request):
    profile= Profile.objects.get(user=request.user)
    if request.method =='POST':
        userform=UserForm(request.POST , instance=request.user)
        profileform=ProfileForm(request.POST, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myform=profileform.save(commit=False)
            messages.success(request, 'Your profile has been updated')
            myform.save()
            return redirect('/formapplication/profile/edit')
    else:
        userform=UserForm( instance=request.user)
        profileform=ProfileForm(instance=profile)
    return render(request,'profile/profile_edit.html',{'userform':userform,'profileform':profileform })