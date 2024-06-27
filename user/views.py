from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import GymUserRegistrationForm, GymUserLoginForm, TrainerRegistrationForm, ClientRegistrationForm
from .models import Trainer, Client, GymUser


def register_view(request):
    if request.method == 'POST':
        gymuser_form = GymUserRegistrationForm(request.POST)
        if gymuser_form.is_valid():
            user = gymuser_form.save()
            user_type = gymuser_form.cleaned_data.get('user_type')
            if user_type == GymUser.TRAINER:
                trainer_form = TrainerRegistrationForm(request.POST)
                if trainer_form.is_valid():
                    trainer = trainer_form.save(commit=False)
                    trainer.user = user
                    trainer.save()
            elif user_type == GymUser.CLIENT:
                client_form = ClientRegistrationForm(request.POST)
                if client_form.is_valid():
                    client = client_form.save(commit=False)
                    client.user = user
                    client.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('home')  # Change 'home' to your home page name
    else:
        gymuser_form = GymUserRegistrationForm()
        trainer_form = TrainerRegistrationForm()
        client_form = ClientRegistrationForm()

    return render(request, 'user/register.html', {
        'gymuser_form': gymuser_form,
        'trainer_form': trainer_form,
        'client_form': client_form
    })


def login_view(request):
    if request.method == 'POST':
        form = GymUserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are now logged in as {username}')
                return redirect('home')  # Change 'home' to your home page name
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = GymUserLoginForm()
    return render(request, 'login.html', {'form': form})