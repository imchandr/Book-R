
from django.contrib import admin
from django.urls import path, include
from reviews.views import home_page_view

urlpatterns = [
    path('', home_page_view, name='home_page'),
    path('admin/', admin.site.urls),
    path('user/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls', namespace='user_account')),
    path('book/', include('reviews.urls', namespace='review')),
    path('blog/', include('blog.urls', namespace='blog')),
  
]
