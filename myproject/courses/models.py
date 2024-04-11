from django.db import models
from django.utils import timezone
# Create your models here.
class CourseCard(models.Model):
    title = models.CharField(max_length=100,default="title")
    image = models.ImageField(upload_to="static/images")
    total_hours = models.FloatField(default=0.00)
    level = models.CharField(max_length=100,default="all")
    vote_count = models.IntegerField(default=0)
    vote_average = models.FloatField(default=0.0)
    last_updated = models.DateTimeField(default=timezone.now)
    date_added = models.DateTimeField(default=timezone.now)
    playlist_resource = models.CharField(max_length=100,default="url")
    
    """ Another Features Just to be in the course page"""
    # prerequisites = models.CharField(max_length=100)
    # description = models.CharField(max_length=100)
    # tags = models.CharField(max_length=100)
    # lessons_num = models.CharField(max_length=100)
    # school = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
