from django.contrib import admin
from django.urls import path
from api.views import student_details,student_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', student_list),
    path('student/<int:pk>/', student_details)
]
