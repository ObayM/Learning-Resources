from django.shortcuts import render
from .models import CourseCard

def home(request):
    # Latest 
    latest_courses = CourseCard.objects.order_by("-last_updated")
    
    # Recommended
    recommended_courses = CourseCard.objects.order_by("-vote_count")
    print(latest_courses[0].title)
    context= {
        "latest_courses" : latest_courses ,
        "recommended_courses" : recommended_courses
    }
    return render(request,'home.html',context)