from django import forms
from .models import Student, Track


# auth imports

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']
        widgets = {

            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),


        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', "last_name", 'age', 'student_track')
        widgets = {

            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            "age": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            "student_track": forms.Select(attrs={'class': 'form-control', 'placeholder': 'Track'}),

        }


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('track_name',)
