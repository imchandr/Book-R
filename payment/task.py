from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from order.models import Order
@shared_task
def email_invoice(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created and payment is completed.
    """
    order = Order.objects.get(id=order_id)
    
    # create invoice e-mail
    subject = f'BOOKR-STORE -  Invoice no. {order.id}'
    message = 'Thank-you for shopping with BOOKR, Please, find invoice attached for your recent purchase.'
    email = EmailMessage(subject,
                         message,
                         'admin@bookr.com',
                         [order.email])
    # generate PDF
    html = render_to_string('order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS('/mnt/HDD/Books/Django-project/Book-R/staticfiles/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out,
                                          stylesheets=stylesheets)
    # attach PDF file
    email.attach(f'order_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')
    # send e-mail
    email.send()