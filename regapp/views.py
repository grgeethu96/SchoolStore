from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from schoolapp.models import Department, Course


def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords are not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def home(request):
    department = Department.objects.all()
    course = Course.objects.all()
    return render(request, 'home.html', {'department': department, 'course': course})


def order(request):
    department = Department.objects.all()
    course = Course.objects.all()
    if request.method == 'POST':
        messages.info(request, "Order Confirmed")
        return render(request, 'order.html')
    else:
        pass
    return render(request, 'order.html', {'department': department, 'course': course})
