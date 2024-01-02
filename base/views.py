from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
# Create your views here.
def home(request):
    profile = Profile.objects.first()
    return render(request, 'base/home.html', {'profile': profile})

def posts(request):
    return render(request, 'base/posts.html')

def post(request):
    return render(request, 'base/post.html')

def profile(request):
    return render(request, 'base/profile.html')
