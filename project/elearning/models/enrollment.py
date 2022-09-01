from django.db import models

from elearning.models.subject_status import SubjectStatus
from .subject import Predmeti
from .user import Myuser
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Enrollment(models.Model):
    usr=models.ForeignKey(Myuser,on_delete=models.CASCADE, blank=True, null=True)
    subject=models.ForeignKey(Predmeti,on_delete=models.CASCADE, blank=True, null=True)
    status=models.ForeignKey(SubjectStatus,on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return '%s:%s' % (self.usr,self.subject)

