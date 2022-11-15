from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import *
from django.template.context_processors import csrf


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


# def register(request):
#       #put a check in place
#     if request.method =='POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data['password1']

#             user = authenticate(username=username, password=password)
#             login(request, user)
            
#             return redirect('login')
#     else:
#         form = UserCreationForm(request.POST)
#     return render(request,'users/register.html',{'form':form})  

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # Profile.get_or_create(user=request.user)
            username = form.cleaned_data.get('username')
            print(username)

            # Automatically Log In The User
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            print(new_user)
            login(request, new_user)
            # return redirect('editprofile')
            return redirect('login')
            

    elif request.user.is_authenticated:
        return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)