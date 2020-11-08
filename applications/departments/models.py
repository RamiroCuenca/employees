from django.db import models

class Department(models.Model):
    name = models.CharField('Name', max_length=50, editable = False)
    tag = models.CharField('Tag', max_length=15, blank = True, unique = True)
    is_active = models.BooleanField('Is Active', default = True)

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.tag + ' - ' + str(self.is_active)