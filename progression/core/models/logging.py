from django.db import models

from .workout import ExerciseConfig


class WorkoutLog(models.Model):
    day = models.DateField(auto_now_add=True)


class ExerciseLog(ExerciseConfig):
    workout = models.ForeignKey(
        WorkoutLog,
        on_delete=models.CASCADE,
    )
    # FEAT orderable
