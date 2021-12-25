
from django.contrib import admin
from django.urls import path, include

from reviews.views import indexView, search_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView),
    path('search', search_book)
    
    
]
