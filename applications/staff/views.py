from django.shortcuts import render

from django.views.generic import (
#    TemplateView,
    ListView,
    CreateView,
    DetailView,
)

# Models
from .models import Staff

class ListAllEmployees(ListView):
    ''' List all employees of the inc '''
    template_name = 'staff/list_employees.html' # The HTML
    model = Staff # The model from where we take the data
    context_object_name = 'listOfEmployees' # The name as we will refere to this at the HTML
    # We can exclude the "context_object_name" and refered to this obj as "object_list" (as default)

    # Usually, if we ask to the DB for more than 20 or 30 results, it will be a really heave query
    # So, using pagination it is helpfull !!
    paginate_by = 4
    # We can manually move forward through the pages
    # http://localhost:8000/list_employees/?page=1 

    # We can also order the elements by them attributes
    ordering = 'id'


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
    

class ListEmployeesKeyWork(ListView):
    ''' List employees by key word '''
    template_name = 'staff/list_keyword.html'
    context_object_name = 'workers'

    def get_queryset(self):
        print('#' * 15)
        kw = self.request.GET.get('kword', '',)
        print('=' * 10, kw)

        list_kw = Staff.objects.filter(
            first_name = kw
        )

        print('Results: ', list_kw)
        return list_kw
    

class ListEmployeesSkills(ListView):
    ''' List employees by their skills '''
    template_name = 'staff/list_skills.html'
    context_object_name = 'skills'

    def get_queryset(self):
        #worker = Staff.objects.get(id=4)
        
        # First we need to catch the kw from the button and input
        kw_name = self.request.GET.get('name')

        # Get the worker whose name matchs
        worker = Staff.objects.get(first_name=kw_name)

        # Filter through the results
        #worker = Staff.objects.get(first_name = kw_name)
        
        return worker.skills.all()


class EmployeeDetailView(DetailView):
    ''' Detail view for one employee '''
    template_name = 'staff/detail_employee.html'
    model = Staff
    # We do not have to add context_object_name
    # by default we can access it from the html as "object"
    # or with the name of the model but without mayus, fe "staff"

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context["tittle"] = 'Employee of the Month' 
        return context
    


class CreateEmployee(CreateView):
    model = Staff
    template_name = "staff/add_employee.html"
    
    # It also needs to know witch attributes we would like to input
    # Also, we can specify each field or use the special attribute "__all__"
    #fields = ['first_name', 'last_name', 'job', 'department', 'avatar', 'description',]
    fields = ('__all__')

    # Also, it does not need a context_object_name, by default we can used it as "form"

    # Watch the HTML and see that it has a lot of methods!