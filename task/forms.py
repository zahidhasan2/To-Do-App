from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model=Task
        exclude=['user']
        
        widgets = {
            'due_date': forms.DateInput(attrs={'type':'date', 'class': 'form-control'}),
            'due_time': forms.TimeInput(attrs={'type':'time', 'class': 'form-control'})
        }
        # widgets = {
        #     'due_date': forms.DateInput(attrs={'class': 'form-control'}, format='%Y-%m-%d'),
        #     'due_time': forms.TimeInput(attrs={'class': 'form-control'}, format='%H:%M'),
        # }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['due_date'].widget.input_type = 'date'
    #     self.fields['due_time'].widget.input_type = 'time'  