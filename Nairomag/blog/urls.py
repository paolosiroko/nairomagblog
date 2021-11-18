from django.urls import path
from .views import BlogView,PostView,CreatePost,UpdatePost,DeletePost,CustomLoginView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('Login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='blog'), name='logout'),

    path('',BlogView.as_view(), name ='blog'),
    path('post/<int:pk>/' ,PostView.as_view(), name='post'),

    path('add/', CreatePost.as_view(), name='add'),
    path('edit/<int:pk>/', UpdatePost.as_view(), name='edit'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete'),
]