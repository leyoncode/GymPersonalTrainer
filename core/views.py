from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'core/home.html', {})

@login_required
def dashboard(request):
    if request.user.user_type == 'Trainer':
        return redirect('trainer_dashboard')
    else:
        return redirect('client_dashboard')