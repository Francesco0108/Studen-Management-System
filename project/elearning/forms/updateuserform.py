from ..models import *
from django.forms import ModelForm
class UpdateUserForm(ModelForm):
    class Meta:
        model=Myuser
        fields=['username','first_name','last_name','email','role','status','is_superuser','is_staff']