from django.db import models

class Izborni(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return '%s' % (self.name)