from django.contrib import admin
from django.urls import path
from api.views import student_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<int:pk>', student_details)
]
