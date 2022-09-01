
from django.db import models
from django.contrib.auth.models import AbstractUser
from .role import Role
from .status import Status

class Myuser(AbstractUser):
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
