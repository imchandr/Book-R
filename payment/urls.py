from django.urls import path
from payment import views
app_name = 'payment'
urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('process/confirm/', views.paymenthandler, name='confirm'),
    
    
]