from django.db import models

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    lessons_num = models.CharField(max_length=100)
    estimated_hours = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    vote_count = models.CharField(max_length=100)
    vote_average = models.CharField(max_length=100)
    prerequisites = models.CharField(max_length=100)
    date = models.DateTimeField()