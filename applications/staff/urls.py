from django.contrib import admin
from django.urls import path, re_path

from .views import ListAllEmployees, ListEmployeesArea

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('list_employees/', ListAllEmployees.as_view()),
    path('list_employees_area/<tag>/', ListEmployeesArea.as_view()), # Send an argument though the url
]