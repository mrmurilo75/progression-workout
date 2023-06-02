from django.db import models

from .exercise import Exercise


class ExerciseConfig(models.Model):
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.PROTECT,
    )
    weight = models.IntegerField()
    # TODO Add measurement
    repetitions = models.SmallIntegerField(default=8)
    series = models.SmallIntegerField(default=3)
    variation = models.BooleanField(default=False)
    notes = models.TextField(max_length=2047, blank=True)

    class Meta:
        abstract = True
