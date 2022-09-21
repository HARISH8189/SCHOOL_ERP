from django.shortcuts import render

# Create your views here.
def add_staff(request):
    return render(request, 'school_admin templates/add_staff.html')

def home(request):
    return render(request, 'school_admin templates/home.html')  

def view_staff(request):
    return render(request, 'school_admin templates/view_staff.html')

def view_student(request):
    return render(request, 'school_admin templates/view_student.html')        
    