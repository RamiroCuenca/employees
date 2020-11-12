from django.contrib import admin
from django.urls import path, re_path

from .views import ListAllEmployees

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('list_employees/', ListAllEmployees.as_view()),
]