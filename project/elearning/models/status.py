from django.db import models

class Status(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return '%s' % (self.name)