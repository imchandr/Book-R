from base64 import urlsafe_b64decode
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.contrib import messages

from django.urls import reverse_lazy
from account.forms import RegistrationForm, UpdateProfileForm, UpdateUserForm
from account.token import account_activation_token
from django.contrib.auth import login
from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str

from order.models import Order
from django.conf import settings
import weasyprint


def account_register(request):

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.first_name = registerForm.cleaned_data['first_name']
            user.last_name = registerForm.cleaned_data['last_name']
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
    return render(request, 'profile/user_profile.html')

def edit_user_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(reverse_lazy('user_account:user_profile'))
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }
        
    return render(request, 'profile/edit_user_profile.html', context)

def user_order(request):
    
    orders = Order.objects.filter(order_account = request.user)
    context = {
        'orders':orders
    }
    return render(request, 'profile/user_order.html', context)


def user_order_detail(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    return render(request, 'profile/user_order_detail.html', {'order':order})

def user_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS(
                                               settings.STATIC_ROOT + '/css/pdf.css')])
    return response

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)
    
