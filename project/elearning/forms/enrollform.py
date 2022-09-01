from ..models import *
from django.forms import ModelForm

class EnrollForm(ModelForm):
    #client=models.ForeignKey('Client',on_delete=models.CASCADE, limit_choices_to={'is_active':True},)
    class Meta:
        model=Enrollment
        fields=['subject','status']
    def __init__(self,subjects,*args, **kwargs):
       super(EnrollForm, self).__init__(*args, **kwargs)
       self.fields['subject'].queryset=subjects