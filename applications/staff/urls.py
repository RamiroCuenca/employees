from django.contrib import admin
from django.urls import path

def hi_staff(self):
    print('STAFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('stafff/', hi_staff)
]
