from django.db import models

class Department(models.Model):
    name = models.CharField('Name', max_length=50, editable = False)
    tag = models.CharField('Tag', max_length=15, blank = True, unique = True)
    is_active = models.BooleanField('Is Active', default = True)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Department'
        ordering = ['-name']
        unique_together = ('name', 'tag')

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.tag + ' - ' + str(self.is_active)