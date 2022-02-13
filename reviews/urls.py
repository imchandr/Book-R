from django.contrib import admin
from django.conf.urls import handler404, handler500
from django.urls import path
from .views import booklist_view, bookdetails_view, bookorder_view, bookorder, delete_review

app_name = 'book'
urlpatterns = [
    path('', booklist_view, name='booklist_view'),
    path('order/', bookorder, name='bookorder'),
    path('<int:id>/order/', bookorder_view, name='bookorder_view'),
    path('<int:id>/', bookdetails_view, name='bookdetails_view'),
    path('delete-review/<int:id>/', delete_review, name='delete_review'),
  
]

handler500 = 'blog.views.handler500'
handler404 = 'blog.views.handler404'