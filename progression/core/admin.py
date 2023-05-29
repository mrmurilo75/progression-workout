from django.contrib import admin

from .models import Exercise, ExerciseConfig, Plan, TrainingDay

admin.site.register(TrainingDay)
admin.site.register(ExerciseConfig)
admin.site.register(Exercise)
admin.site.register(Plan)
