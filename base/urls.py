from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name='home'),
path('contact/', views.contact, name='contact'),
path('posts/', views.posts, name='posts'),
path('post/', views.post, name='post'),
path('profile/', views.profile, name='profile')
]