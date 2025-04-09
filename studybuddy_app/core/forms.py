from django import forms
from .models import Assignment, WellnessCheck
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'due_date', 'status']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class WellnessCheckForm(forms.ModelForm):
    class Meta:
        model = WellnessCheck
        fields = ['mood', 'stress_level', 'notes']

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
