from django.db import models

from elearning.models.izborni import Izborni
from .user import Myuser
from .program import Program

class Predmeti(models.Model):
    #IZBORNI = (('DA', 'da'), ('NE', 'ne'))
    name = models.CharField(max_length=50)
    kod = models.CharField(max_length=50)
    program = models.ForeignKey(Program,on_delete=models.CASCADE)
    ects = models.IntegerField()
    sem_red = models.IntegerField()
    sem_izv = models.IntegerField()
    izborni = models.ForeignKey(Izborni,on_delete=models.CASCADE)
    nositelj=models.ForeignKey(Myuser,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return '%s' % (self.name)

