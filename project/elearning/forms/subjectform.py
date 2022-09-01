from ..models import *
from django.forms import ModelForm

class SubjectForm(ModelForm):
    class Meta:
        model=Predmeti
        fields=['name','kod','program','ects','sem_red','sem_izv','izborni','nositelj']
    def __init__(self,professors,*args, **kwargs):
       super(SubjectForm, self).__init__(*args, **kwargs)
       self.fields['nositelj'].queryset=professors