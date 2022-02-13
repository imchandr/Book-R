from django.urls import path
from django.conf.urls import handler404, handler500
from account.forms import LoginForm, ResetPasswordForm, ResetPasswordConfirmForm, ChangePasswordForm
from account.views import account_register, account_activate, user_profile,edit_user_profile
from django.contrib.auth import views as auth_view

app_name = 'user_account'
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name="registration/login.html",
                                               authentication_form=LoginForm), name='login'),
    path('register/', account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/',
         account_activate, name='activate'),
    path('reset-password/', auth_view.PasswordResetView.as_view(template_name='registration/password_reset.html',
         form_class=ResetPasswordForm), name='reset_password'),
    path('reset-password-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html', form_class=ResetPasswordConfirmForm), name='reset_password_confirm'),
    path('profile/',user_profile, name='user_profile'),
    path('profile/edit/',edit_user_profile, name='edit_user_profile'),
    path('change-password/', auth_view.PasswordChangeView.as_view(
        template_name='registration/change_password.html', form_class=ChangePasswordForm), name='change_password'),



]

handler500 = 'blog.views.handler500'
handler404 = 'blog.views.handler404'