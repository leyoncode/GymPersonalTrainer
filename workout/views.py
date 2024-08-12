from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from user.models import Trainer, GymUser
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm


@login_required
def trainer_dashboard(request):
    if request.user.user_type != 'Trainer':
        return redirect('client_dashboard')

    trainer_instance = Trainer.objects.get(user=request.user)
    # Fetch workouts where the trainer is the logged-in user
    workouts = Workout.objects.filter(trainer=trainer_instance)

    return render(request, 'workout/trainer_dashboard.html', {'workouts': workouts})


@login_required
def client_dashboard(request):
    workouts = Workout.objects.filter(client=request.user.client)
    return render(request, 'workout/client_dashboard.html', {'workouts': workouts})


@login_required
def create_workout(request):
    trainer = request.user.trainer  # Assuming a Trainer profile is linked directly to User model
    if request.method == 'POST':
        form = WorkoutForm(request.POST, trainer=trainer)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.trainer = trainer  # Set the trainer as the currently logged-in trainer
            workout.save()
            return redirect('trainer_dashboard')
    else:
        form = WorkoutForm(trainer=trainer)
    return render(request, 'workout/create_workout.html', {'form': form})

@login_required
def edit_workout(request, workout_id):
    trainer = request.user.trainer
    workout = get_object_or_404(Workout, id=workout_id, trainer=trainer)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout, trainer=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer_dashboard')
    else:
        form = WorkoutForm(instance=workout, trainer=trainer)
    return render(request, 'workout/edit_workout.html', {'form': form})


@login_required
def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, trainer=request.user.trainer)
    workout.delete()
    return redirect('trainer_dashboard')


@login_required
def workout_detail(request, workout_id):
    # Get the user and determine their role
    user_type = request.user.user_type

    # Define the workout query based on user type
    if user_type == GymUser.TRAINER:
        # Ensure that the workout is associated with the trainer
        workout = get_object_or_404(Workout, id=workout_id, trainer__user=request.user)
    elif user_type == GymUser.CLIENT:
        # Ensure that the workout is associated with the client
        workout = get_object_or_404(Workout, id=workout_id, client__user=request.user)
    else:
        return redirect('home')  # Redirect if the user type is neither Trainer nor Client

    # Fetch the exercises for the validated workout
    exercises = Exercise.objects.filter(workout=workout)

    return render(request, 'workout/workout_detail.html', {'workout': workout, 'exercises': exercises})



@login_required
def create_exercise(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.workout = workout  # Set the workout automatically
            exercise.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = ExerciseForm()

    return render(request, 'workout/create_exercise.html', {'form': form, 'workout': workout})