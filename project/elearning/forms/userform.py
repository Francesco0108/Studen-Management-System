from ..models import *
from django.forms import ModelForm
class UserForm(ModelForm):
    class Meta:
        model=Myuser
        fields=['username','first_name','last_name','email','password','role','status','is_superuser','is_staff']
