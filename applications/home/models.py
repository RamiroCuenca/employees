from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    amount = models.IntegerField() 

    def __str__(self):
        return self.title + ' - ' + self.subtitle + ' - ' + str(self.amount)