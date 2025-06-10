from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.


def home(request):
    return render(request, 'index.html')



def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {"error": "Invalid credentials"})
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):

    if request.method=="POST":
        full_name=request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username, email=email).exists():
            return render(request, 'signup.html', {'error': 'user already exists'})
        
        user = User.objects.create_user(first_name=full_name,
                                         username=username,
                                           email=email,
                                           password=password
                                        )
        user.save()
        return redirect('login')

    return render(request, 'signup.html')




def post(request):
    return render(request, 'post.html')
