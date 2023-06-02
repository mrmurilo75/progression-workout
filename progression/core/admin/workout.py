from django.contrib import admin

from ..models import Plan, Workout, ExerciseSetup


class ExerciseSetupInline(admin.TabularInline):
    model = ExerciseSetup
    fk_name = "workout"


class WorkoutInline(admin.TabularInline):
    model = Workout
    fk_name = "plan"


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    inlines = [WorkoutInline]


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "plan"]
    list_filter = ["plan"]
    inlines = [ExerciseSetupInline]
