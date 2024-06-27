from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import GymUserRegistrationForm, GymUserLoginForm, TrainerRegistrationForm, ClientRegistrationForm
from .models import Trainer, Client, GymUser


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import GymUserRegistrationForm, TrainerRegistrationForm, ClientRegistrationForm
from .models import GymUser


def register_view(request):
    if request.method == 'POST':
        gymuser_form = GymUserRegistrationForm(request.POST)
        trainer_form = TrainerRegistrationForm(request.POST)
        client_form = ClientRegistrationForm(request.POST)

        if gymuser_form.is_valid():
            user = gymuser_form.save()
            user_type = gymuser_form.cleaned_data.get('user_type')

            if user_type == GymUser.TRAINER and trainer_form.is_valid():
                trainer = trainer_form.save(commit=False)
                trainer.user = user
                trainer.save()
            elif user_type == GymUser.CLIENT and client_form.is_valid():
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

    context = {
        'gymuser_form': gymuser_form,
        'trainer_form': trainer_form,
        'client_form': client_form
    }
    return render(request, 'user/register.html', context)  # Change 'your_template.html' to your actual template name



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
    return render(request, 'user/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')