from django.contrib import admin
from django.urls import path

def apps(self):
    print('HOLLLLLLLLLLLLLLLLLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA APPS')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('departments/', apps),
]
