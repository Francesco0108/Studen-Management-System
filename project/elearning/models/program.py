from django.db import models

class Program(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return '%s' % (self.name)