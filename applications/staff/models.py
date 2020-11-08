from django.db import models

from applications.departments.models import Department

class Staff(models.Model):
    ''' Model for employees table '''

    JOB_CHOICES = (
        ('0', 'Marketer'),
        ('1', 'Administrator'),
        ('2', 'HR Specialist'),
        ('3', 'Accountant'),
        ('4', 'Worker'),
        ('5', 'Salesman'),
        ('6', 'Other'),
    )

    first_name = models.CharField('Name', max_length = 50)
    last_name = models.CharField('Last Name', max_length = 50)
    job = models.CharField('Job', max_length = 1, choices = JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.job  