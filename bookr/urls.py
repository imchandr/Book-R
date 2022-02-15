
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from reviews.views import home_page_view

urlpatterns = [
    path('', home_page_view, name='home_page'),
    path('admin/', admin.site.urls),
    
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('order.urls', namespace='orders')),
    
    path('user/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls', namespace='user_account')),
    path('book/', include('reviews.urls', namespace='review')),
    path('blog/', include('blog.urls', namespace='blog')),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
