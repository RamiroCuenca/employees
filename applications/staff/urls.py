from django.contrib import admin
from django.urls import path, re_path

from .views import (
    ListAllEmployees, ListEmployeesArea, ListEmployeesJob, ListEmployeesKeyWork,
    ListEmployeesSkills,
)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('list_employees/', ListAllEmployees.as_view()),
    path('list_employees_area/<tag>/', ListEmployeesArea.as_view()), # Send an argument though the url
    path('list_employees_job/<task>/', ListEmployeesJob.as_view()),
    path('list_keyword/', ListEmployeesKeyWork.as_view()),
    path('list_skills/', ListEmployeesSkills.as_view())
]