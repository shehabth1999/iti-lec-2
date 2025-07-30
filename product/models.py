from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=52, null=False, default="Title")
    instructor = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    duration = models.IntegerField(null=False, default=0)
    price = models.FloatField(null=False, default=0)

    def __str__(self):
        return f"{self.title}"

class Student(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
    ]
    
    name = models.CharField(max_length=52, null=False, default="Name")
    age = models.IntegerField(null=False, default=0)
    email = models.EmailField(null=False, unique=True)
    is_active = models.BooleanField(null=False, default=True)
    grade = models.FloatField(null=True)
    course = models.ForeignKey(Course, related_name="students", on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='students/', null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, null=False, default="male")
    is_graduated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"        