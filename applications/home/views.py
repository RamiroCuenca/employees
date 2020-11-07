from django.shortcuts import render

# Generic views from Django
from django.views.generic import TemplateView

# We work with classes as views
class TestView(TemplateView):
    template_name = 'test.html' # Remember to create the template
