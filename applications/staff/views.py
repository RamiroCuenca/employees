from django.shortcuts import render

from django.views.generic import (
#    TemplateView,
    ListView,
#    CreateView,
)

# Models
from .models import Staff

class ListAllEmployees(ListView):
    ''' List all employees of the inc '''
    template_name = 'staff/list_employees.html' # The HTML
    model = Staff # The model from where we take the data
    context_object_name = 'listOfEmployees' # The name as we will refere to this at the HTML