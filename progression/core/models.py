from django.db import models


class TrainingDay(models.Model):
    name = models.CharField(max_length=127)


class TrainingExercise(models.Model):
    training_day = models.ForeignKey(
        TrainingDay,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=127)
    description = models.TextField(max_length=1023, blank=True)
    weight = models.IntegerField()
    repetitions = models.SmallIntegerField(default=3)
    series = models.SmallIntegerField(default=3)

