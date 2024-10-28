from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('category/<str:tag>/', home_view, name='category'),
    path('post/create/', post_create_view, name='post-create'),
    path('post/delete/<str:pk>/', post_delete_view, name='post-delete'),
    path('post/edit/<str:pk>/', post_edit_view, name='post-edit'),
    path('post/<str:pk>/', post_page_view, name='post'),
    path('post/like/<str:pk>/', like_post, name='like-post'),
    path('commentsent/<str:pk>/', comment_sent, name='comment-sent'),
    path('comment/like/<str:pk>/', like_comment, name='like-comment'),
    path('comment/delete/<str:pk>/', comment_delete_view, name='comment-delete'),
    path('reply-sent/<str:pk>/', reply_sent, name='reply-sent'),
    path('reply/like/<str:pk>/', like_reply, name='like-reply'),
    path('reply/delete/<str:pk>/', reply_delete_view, name='reply-delete'),
]