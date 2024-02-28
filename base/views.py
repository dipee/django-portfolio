from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import ContactModelForm
from .models import Profile, Project, Skill
# Create your views here.
def home(request):
    user_profile = Profile.objects.first()
    projects = Project.objects.all()
    user_form = ContactModelForm()
    skills = Skill.objects.all()
    return render(request, 'base/home.html', {
        'profile': user_profile, 'form': user_form, 'projects': projects, 'skills': skills
    })

def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()

        return JsonResponse({"message": f"Thank you {form.cleaned_data.get("name")} for your message."})
    return JsonResponse({"message": "Error saving message."})
def posts(request):
    return render(request, 'base/posts.html')

def post(request):
    return render(request, 'base/post.html')

def profile(request):
    return render(request, 'base/profile.html')
