from django.shortcuts import render

# Create your views here.
def index(request):
    user = request.user
    context = {
        'user': user
    }
    print(user.is_authenticated)
    return render(request, "index.html",context)