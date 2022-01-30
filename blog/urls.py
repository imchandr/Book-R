from django.urls import path
from blog.views import post_list, post_detail, post_share, tailwind

app_name = 'blog'
urlpatterns = [
    path('',post_list, name='post_list'),
    path('tailwind', tailwind),
    path('<slug:post>/',post_detail,name='post_detail'),
    path('<slug:post>/share/',post_share,name='post_share'),
]
