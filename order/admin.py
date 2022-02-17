from django.contrib import admin
from order.models import Order, OrderItem
from django.urls import reverse
from django.utils.safestring import mark_safe

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

def order_detail(obj):
    url = reverse('orders:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">View</a>')
 
def order_pdf(obj):
    url = reverse('orders:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')
order_pdf.short_description = 'Invoice'
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email',
                    'street', 'city', 'state', 'zip',
                    'created', 'updated','paid','transection_id',order_detail,order_pdf]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    
@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']
    
    
    