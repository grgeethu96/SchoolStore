from .models import Department, Course
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    department = Department.objects.all()
    return render(request, 'index.html', {"department": department})


