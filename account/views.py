from base64 import urlsafe_b64decode
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic

from django.urls import reverse_lazy
from account.forms import RegistrationForm
from account.token import account_activation_token
from django.contrib.auth import login
from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str




def account_register(request):

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate your Book-R account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'tocken': account_activation_token.make_token(user)
            })
            user.email_user(subject=subject, message=message)
            return render(request,'registration/activation_sucess.html')
        else:
            registerForm.errors
    else:
        registerForm = RegistrationForm()
            
    return render(request, 'registration/register.html', {'form': registerForm })

def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active =True
        user.save()
        login(request, user)
        # return render(request, 'home_page')
        # return HttpResponse('welcome to booker')
        return redirect('home_page')
    else:
        return render(request, 'registration/activation_invalid.html')

def user_profile(request):
    context = {
        
    }
    return render(request, 'profile/user_profile.html', context)


    
