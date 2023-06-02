from django.contrib import admin

from ..models import WorkoutLog, ExerciseExecutionLog


class ExerciseExecutionLogInline(admin.TabularInline):
    model = ExerciseExecutionLog
    fk_name = "workout_log"


@admin.register(WorkoutLog)
class WorkoutLogAdmin(admin.ModelAdmin):
    list_display = ["datetime", "workout"]
    list_filter = ["workout"]
    inlines = [ExerciseExecutionLogInline]
