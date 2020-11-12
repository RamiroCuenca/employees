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
    # We can exclude the "context_object_name" and refered to this obj as "object_list" (as default)

class ListEmployeesArea(ListView):
    ''' List of employees which belong to x area '''
    template_name = 'staff/list_employees_area.html'
    context_object_name = 'listByArea'
    #model = Staff

    ''' Probably de worst way of filtering v
    queryset = Staff.objects.filter(
        # Queryset allow as to specify with wich attribute we want to make the list!!
        department__name = 'Administration' # Note that we use 2 under_score
    )
    '''
    
    def get_queryset(self): # Predeterminate function
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        # To catch the arg from the url v
        tag_area = self.kwargs['tag']

        listArea = Staff.objects.filter(
            # Queryset allow as to specify with wich attribute we want to make the list!!
            # department__tag = 'ADM' # Note that we use 2 under_score
            department__tag = tag_area 
        )
        # Quiet with the fact that it it does not return a list (1 object) it cause an error!
        return listArea # Returns a list


class ListEmployeesJob(ListView):
    ''' List employees by job they do '''
    template_name = 'staff/list_employees_job.html'
    context_object_name = 'listEmpJob'

    def get_queryset(self):
        # Catch the job through the url
        job_task = self.kwargs['task']
        # Make the filter
        listJob = Staff.objects.filter(
            job = job_task
            )
        return listJob
    

