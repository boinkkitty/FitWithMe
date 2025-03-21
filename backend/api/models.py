from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True) # Email
    height = models.FloatField() # Height in cm
    weight = models.FloatField() # Weight in kg

    def __str__(self):
        return self.username

class TemplateWorkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workout_templates") # User tagged to workout template
    name = models.CharField(max_length=100) # Name of template

    def __str__(self):
        return self.name

class TemplateExercise(models.Model):
    template = models.ForeignKey(TemplateWorkout, on_delete=models.CASCADE, related_name="exercises") # Template ID
    name = models.CharField(max_length=100) # Name of exercise
    sets = models.IntegerField(default=3, validators=[MinValueValidator(1)]) #Usual number of sets

    def __str__(self):
        return f"{self.name}"
    
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts") #User ID
    name = models.CharField(max_length=100) # Name of workout
    workout_date = models.DateTimeField() # Workout date

    def __str__(self):
        return {self.name}

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises")
    name = models.CharField(max_length=100) # Name of exercise
    weights = models.FloatField() # Weight in kg
    reps = models.IntegerField(validators=[MinValueValidator(1)]) # Number of reps

    def __str__(self):
        return f"{self.name}"