from django.contrib import admin
from django.urls import path, re_path

from .views import (
    ListAllEmployees, ListEmployeesArea, ListEmployeesJob, ListEmployeesKeyWork,
    ListEmployeesSkills, EmployeeDetailView, CreateEmployee, SuccessCreateEmployee,
)

app_name = "staff_app" # Used in 'reverse_lazy()' to refere to this file

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('list_employees/', ListAllEmployees.as_view()),
    path('list_employees_area/<tag>/', ListEmployeesArea.as_view()), # Send an argument though the url
    path('list_employees_job/<task>/', ListEmployeesJob.as_view()),
    path('list_keyword/', ListEmployeesKeyWork.as_view()),
    path('list_skills/', ListEmployeesSkills.as_view()),
    path('detail_employee/<pk>/', EmployeeDetailView.as_view()), # By default it accepts pk arg
    path('create_employee/', CreateEmployee.as_view()),
    path('success_add/', SuccessCreateEmployee.as_view(), name='success'),
]