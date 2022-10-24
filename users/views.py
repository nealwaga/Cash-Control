from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.

@login_required
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        profile_form = ProfileUpdateForm (request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')
    else:
        profile_form = ProfileUpdateForm (instance=request.user.profile)
    context = {
        'current_user': current_user,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)