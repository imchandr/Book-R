from django.contrib import admin
from django.urls import path
from .views import  welcome_view, booklist_view, bookdetails_view

urlpatterns = [

    path('', welcome_view, name='welcome_view',),
    path('books/', booklist_view, name='booklist_view'),
    path('books/<int:id>/', bookdetails_view, name='bookdetails_view')

]