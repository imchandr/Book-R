
from urllib import response
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from order.models import Order
from cart.cart import Cart
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest

import weasyprint
from io import BytesIO
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from payment.task import email_invoice
import razorpay

# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    

    razor_order = razorpay_client.order.create(
    dict( amount=int(total_cost*100), currency='INR', payment_capture='0'))
    razor_order_id = razor_order['id']
    callback_url = 'confirm/'

    context = {
    'razor_order_id': razor_order_id,
    'razor_api_key': settings.RAZOR_KEY_ID,
    'amount': int(total_cost*100),
    'currency': 'INR',
    'callback_url': callback_url
    }


    return render(request, 'payment/process.html', context)

@csrf_exempt
def paymenthandler(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    send_mail = False
    
    
    if request.method == 'POST':
        try:
         # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            
            if result:
                
                order.paid = True
                # store the unique transaction id
                order.transection_id = payment_id
                order.save()
                
                # asynk task that emails order invoice 
                email_invoice.delay(order.id)
               
          
                # # render success page on successful caputre of payment
                return render(request, 'payment/done.html',{'transection':payment_id})
            
             
                
            else:

                # if signature verification fails.
                return render(request, 'payment/payment_error.html')
        except:

            # if we don't find the required parameters in POST data
            return HttpResponse('Invalid Parameter from POST')
    else:
       # if other than POST request is made.
        return HttpResponse("Didn't rerceive POST request from RazorPay")
    
    



def test(request):
    return render(request, 'payment/payment_error.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
