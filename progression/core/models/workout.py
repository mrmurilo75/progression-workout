from django.db import models

from .base import ExerciseConfig


class Plan(models.Model):
    name = models.CharField(max_length=127)


class Workout(models.Model):
    name = models.CharField(max_length=127)
    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
    )
    # FEAT Add orderable to dj-adm
    # FEAT ADV Change m2m for reusable in multiple Plan's


class ExerciseSetup(ExerciseConfig):
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
    )
