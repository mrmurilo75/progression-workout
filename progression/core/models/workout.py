from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField(max_length=1023, blank=True)
    # FEAT Add more media fields for better description


class ExerciseConfig(models.Model):
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.PROTECT,
    )
    weight = models.IntegerField()
    repetitions = models.SmallIntegerField(default=8)
    series = models.SmallIntegerField(default=3)


class Workout(models.Model):
    name = models.CharField(max_length=127)
    exercises = models.ManyToManyField(ExerciseConfig, related_name="+")
    # FEAT Add orderable to dj-adm


class Plan(models.Model):
    name = models.CharField(max_length=127)
    workout_set = models.ManyToManyField(Workout)
