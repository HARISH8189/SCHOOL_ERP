from django.urls import path
from . import views

urlpatterns=[
    path('add_staff',views.add_staff),
    path('home',views.home),
    path('view_staff',views.view_staff),
    path('view_student',views.view_student)
]