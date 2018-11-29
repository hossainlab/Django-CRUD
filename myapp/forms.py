from .models import Developer 
from django import forms 

class DeveloperForm(forms.ModelForm): 
    class Meta: 
        model = Developer
        fields = ['name', 'email', 'phone']