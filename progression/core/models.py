from django.db import models
from model_utils.models import TimeStampedModel


# We have a Plan
#           |_ Have a few Days
#                          |_ Each a set of Compound Exercise -> compromised of
#                                       [Exercise][Weight][Repetitions][Series]
#                                           -> The same exercise can have more then 1 configuration,
#                                              but it should still be the same exercise


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
    repetitions = models.SmallIntegerField(default=3)
    series = models.SmallIntegerField(default=3)


class Plan(models.Model):
    name = models.CharField(max_length=127)


class TrainingDay(models.Model):
    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=127)
    exercises = models.ManyToManyField(ExerciseConfig)


# We should be able to mark when we done each exercise
#       One way to do this, would be,
#           once we mark the first time as done,
#           we make a copy of that given configuration
#           (possibly just a json field with all the configs)


class TrainingDayLog(models.Model):
    day = models.DateField(auto_now_add=True)


class ExerciseLog(ExerciseConfig):
    train = models.ForeignKey(
        TrainingDayLog,
        on_delete=models.CASCADE,
    )
