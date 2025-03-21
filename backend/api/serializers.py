from rest_framework import serializers
from api.models import User, TemplateWorkout, TemplateExercise, Workout, Exercise

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'height', 'weight']

class TemplateWorkoutSerializers(serializers.ModelSerializer):
    class Meta:
        model = TemplateWorkout
        fields = ['id', 'user', 'model']

class TemplateExerciseSerializers(serializers.ModelSerializer):
    class Meta:
        model = TemplateExercise
        fields = ['id', 'template', 'name', 'sets']

class WorkoutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'user', 'name', 'workout_date']

class ExerciseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'workout', 'name', 'weights', 'reps']