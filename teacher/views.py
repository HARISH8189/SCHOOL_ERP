from django.shortcuts import render

# Create your views here.
def add_student(request):
    return render(request, 'teacher templates/add_student.html')

def change_password(request):
    return render(request, 'teacher templates/change_password')

def home(request):
    return render(request, 'teacher templates/home.html')

def view_student(request):
    return render(request, 'teacher templates/view_student.html')       


