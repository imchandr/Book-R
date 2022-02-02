from django.contrib import admin
from django.urls import path
from .views import booklist_view, bookdetails_view, add_review_view

app_name = 'book'
urlpatterns = [

    
    path('', booklist_view, name='booklist_view'),
    path('<int:id>/', bookdetails_view, name='bookdetails_view'),
    path('<int:id>/add-review/', add_review_view, name='add_review')

]