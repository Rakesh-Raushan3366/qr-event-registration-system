from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.contrib.auth import logout
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.

# User Registration view function
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# User Login view function
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, f'You are now logged in as {user.email}!')
            return redirect('register_shatabdi')
        else:
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'login.html')

# User Logout view function
def user_logout(request):
    logout(request)
    return redirect('login')