from django.contrib import admin
from django.urls import path
from .views import booklist_view, bookdetails_view

app_name = 'book'
urlpatterns = [
    path('', booklist_view, name='booklist_view'),
    path('<int:id>/', bookdetails_view, name='bookdetails_view'),
  
]