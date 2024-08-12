from django.urls import path
from .views import trainer_dashboard, create_workout, edit_workout, delete_workout, workout_detail, client_dashboard, create_exercise

urlpatterns = [
    path('trainer/dashboard/', trainer_dashboard, name='trainer_dashboard'),
    path('client/dashboard/', client_dashboard, name='client_dashboard'),
    path('workout/create/', create_workout, name='create_workout'),
    path('workout/edit/<int:workout_id>/', edit_workout, name='edit_workout'),
    path('workout/delete/<int:workout_id>/', delete_workout, name='delete_workout'),
    path('workout/<int:workout_id>/', workout_detail, name='workout_detail'),
    path('exercise/create/<int:workout_id>/', create_exercise, name='create_exercise'),

]