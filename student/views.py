from django.shortcuts import render

# Create your views here.
def change_password(request):
    return render(request, 'student_templates/change_password.html')

def profile(request):
    return render(request, 'student_templates/profile.html')

def student_home(request):
    return render(request, 'student_templates/student_home.html')        