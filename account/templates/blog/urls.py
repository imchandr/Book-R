from django.urls import path
from django.conf.urls import handler404, handler500
from blog.views import PostCreate,PostUpdate,PostDelete,CommentDelete,post_list, post_detail, post_share, tailwind


app_name = 'blog'
urlpatterns = [
    path('create/',PostCreate.as_view(),name='create_post'),
    path('<int:pk>/update/',PostUpdate.as_view(),name='update_post'),
    path('<int:pk>/delete/',PostDelete.as_view(),name='delete_post'),
    path('<slug:post>/delete-comment/<int:pk>/',CommentDelete.as_view(),name='delete_comment'),
    path('',post_list, name='post_list'),
    path('<slug:post>/',post_detail,name='post_detail'),
    path('<slug:post>/share/',post_share,name='post_share'),
    path('tailwind', tailwind),
]

handler500 = 'blog.views.handler500'
handler404 = 'blog.views.handler404'
