from django.contrib import admin
from django.urls import path
from .views import booklist_view, bookdetails_view, bookorder_view, bookorder

app_name = 'book'
urlpatterns = [
    path('', booklist_view, name='booklist_view'),
    path('order/', bookorder, name='bookorder'),
    path('<int:id>/order/', bookorder_view, name='bookorder_view'),
    path('<int:id>/', bookdetails_view, name='bookdetails_view'),
  
]