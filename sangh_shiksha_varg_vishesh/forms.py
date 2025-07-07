
from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.models import Group # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.core.validators import RegexValidator # type: ignore
from .models import *

# Create your forms here.

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



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegisterSamautkarshRegistration
        fields = ['name','last_name', 'dob',  'phone_number', 'gender', 'blood_group', 'corress_address','perman_address','address_pincode','address_state','ekai_milaan','ekai_sakha_milan', 'nagar_address', 'pincode', 'user_type', 'ekai_mandal', 'referral_code','vividhsangathan','ekai_basti','state','ekai_upbasti','ekai','ekai_nagar','dayitv','nagar','prant','vibhag','jila']

class EventRegisterForm(forms.ModelForm):
    class Meta:
        model = EventForm
        fields = "__all__"

class MobileForm(forms.Form):
    mobile = forms.CharField(max_length=10, min_length=10, required=True)

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, min_length=6, required=True)

class barcodsForm(forms.ModelForm):
    class Meta:
        model = BarcodeScan
        fields = ['name','phone_number','nagar','dayitv','qrcode']

class ScannedPersonForm(forms.ModelForm):
    class Meta:
        model = ScannedPerson
        fields = ['phone_number','person_scanned']


class EventGhoshForm(forms.ModelForm):
    class Meta:
        model = GhoshEvent
        fields = "__all__"

class EventSamanyaForm(forms.ModelForm):
    class Meta:
        model = ShikshanSamanyaEvent
        fields = "__all__"

class EventVisheshForm(forms.ModelForm):
    class Meta:
        model = ShikshanVisheshEvent
        fields = "__all__"


class EventKaryakartaViskasVargPrathamSamanyaForm(forms.ModelForm):
    class Meta:
        model = KaryakartaViskasVargPrathamSamanyaEvent
        fields = "__all__"


