from django.db import models

from applications.departments.models import Department


class Skills(models.Model):
    ''' Skills each worker have '''
    skill = models.CharField('Skill', max_length=50)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return str(self.id) + ' - ' + self.skill


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
    avatar = models.ImageField(upload_to='staff', blank = True, null = True, height_field=None, width_field=None, max_length=None)
    skills = models.ManyToManyField(Skills)

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Staff'
        ordering = ['job']
        unique_together = ('first_name', 'last_name')


    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.job  