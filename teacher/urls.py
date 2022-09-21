from django.urls import path
from . import views

urlpatterns=[
    path('add_student',views.add_student),
    path('change_password',views.change_password),
    path('home',views.home),
    path('view_student',views.view_student)
]