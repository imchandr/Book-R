from django.urls import path
from account.forms import LoginForm
from account.views import UserRegisterView
from django.contrib.auth import views as auth_view

app_name = 'user_account'
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name="registration/login.html",
                                                authentication_form=LoginForm), name='login'),
    path('register/',UserRegisterView.as_view(), name='register'),
    
    

]