from django.shortcuts import render

# Generic views from Django
from django.views.generic import TemplateView, ListView

'''
Django works with class based views
There are different generic views, some of them are:
> TemplateView --> Have a "template_name" var wich associate the 
view with a html file located always in "templates" folder  
> ListView --> Used to list objects or records
> CreateView
> UpdateView
'''
class TestView(TemplateView):
    template_name = 'home/test.html' # Remember to create the template


class TestListView(ListView):
    template_name = "home/list.html"
    context_object_name = 'listOfNumbers' # Like a var declaration, we refere to it at the HTML as the queryset
    # model = Test # Model from DB 
    queryset = ['0', '10', '20', '30', '40', '50']
