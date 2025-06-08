from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import Reg_user

def reg(request):
    if request.method == 'POST':
        name     = request.POST.get('name')
        email    = request.POST.get('email')
        password = request.POST.get('password')

        # 1. Check if username OR email already exist
        if User.objects.filter(username=name).exists():
            return render(request, 'register.html', {
                'error': "Username already taken!",
                'css': 'login.css',
                'title': 'Register'
            })
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {
                'error': "Email already registered!",
                'css': 'login.css',
                'title': 'Register'
            })

        # 2. Create the Django user
        user = User.objects.create_user(username=name, email=email, password=password)

        # 3. Create your profile record
        Reg_user.objects.create(user=user, name=name, email=email)

        # 4. Redirect to login (or auto-login if you prefer)
        return redirect('login')

    # GET
    return render(request, 'register.html', {
        'css': 'login.css',
        'title': 'Register'
    })


def login(request):
    
    
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        if Reg_user.objects.filter(name=name):
        
        # Authenticate user using Django's built-in authenticate method
            user = authenticate( request,username=name, password=password)
            if user is None:
                return redirect('login')
            else:
                auth_login(request, user)  # This logs in the user and creates a session
                return redirect('dashboard')
        else:
            return redirect('reg')


    css = 'login.css'
    title = 'Login'
    context = {'css':css,'title':title}
    return render(request, 'login.html',context)



