"""
VERSION: 0.1.0

Ok, so a Plan has a few workouts, these could be used in other Plans, but lets simplify
Then each workout has an ExerciseSetup that has the ExerciseConfig fields
The ExerciseConfig has the information do perform an exercise and points to an Exercise

A workout logging has a time and date, and contains the ExerciseExecutionLog, which also has a time and date,
and the ExerciseConfig fields.

ExerciseConfig M->1 Exercise

Plan 1<-M Workout 1<-M ExerciseSetup(ExConfig)
          ^ 1
         / M
WorkoutLog M<-M ExerciseExecutionLog(ExConfig)

"""

from .exercise import Exercise
from .logging import ExerciseExecutionLog, WorkoutLog
from .workout import Workout, Plan, ExerciseSetup
