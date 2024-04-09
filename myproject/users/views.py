from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib import messages

# Create your views here.
def profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, "profile.html",context)

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('profile')

        else:
            return redirect('/')

    return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        my_user = User.objects.create_user(username=username,password=password)
        
        my_user.first_name = fname
        my_user.last_name = lname

        my_user.save()

        return redirect("login")
    return render(request, "signup.html")

def signout(request):
    logout(request)
    return redirect("index")