from django.db import models

from .base import ExerciseConfig
from .workout import Workout


class WorkoutLog(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
    )


class ExerciseExecutionLog(ExerciseConfig):
    datetime = models.DateTimeField(auto_now_add=True)
    workout_log = models.ForeignKey(
        WorkoutLog,
        on_delete=models.CASCADE,
    )
    # FEAT orderable
