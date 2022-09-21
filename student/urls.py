from django.urls import path
from . import views

urlpatterns=[
    path('change_password',views.change_password),
    path('profile',views.profile),
    path('student_home',views.student_home)
]