from django.contrib import admin
from .models import CourseCard

@admin.register(CourseCard)
class CourseCard(admin.ModelAdmin):
    list_display = ['title']
