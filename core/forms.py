from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import *


# Create your forms here.

# User Registration Form
class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email address already registered.')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already taken.')
        return username
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password1
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2

    
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class MobileForm(forms.Form):
    mobile = forms.CharField(max_length=10, min_length=10, required=True)

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, min_length=6, required=True)


class RoleManagementForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['name', 'mobile', 'role', 'role_level', 'role_sublevel']

    role = forms.ChoiceField(
        choices=[(role, role) for role in Admin.objects.values_list('role', flat=True).distinct()],
        required=True
    )
    role_level = forms.ChoiceField(
        choices=[(role_level, role_level) for role_level in Admin.objects.values_list('role_level', flat=True).distinct()],
        required=True
    )
    role_sublevel = forms.ChoiceField(
        choices=[(role_sublevel, role_sublevel) for role_sublevel in Admin.objects.values_list('role_sublevel', flat=True).distinct()],
        required=True
    )


class ScannedPersonForm(forms.ModelForm):
    class Meta:
        model = ScannedPerson
        fields = ['mobile','person_scanned']

   
        
