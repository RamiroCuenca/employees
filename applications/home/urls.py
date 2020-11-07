from django.contrib import admin
from django.urls import path

# Import views from this folder
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('test/', views.TestView.as_view()),
    path('list/', views.TestListView.as_view()),
    path('test_list/', views.TestList.as_view()),
]
