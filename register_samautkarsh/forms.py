
from django import forms
from .models import *

# Create your forms here.

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegisterSamautkarshRegistration
        fields = "__all__"
        #fields = ['name','last_name', 'dob',  'phone_number', 'gender', 'blood_group', 'corress_address','perman_address','address_pincode','address_state','ekai_milaan','ekai_sakha_milan', 'nagar_address', 'pincode', 'user_type', 'ekai_mandal', 'referral_code','vividhsangathan','ekai_basti','state','ekai_upbasti','ekai','ekai_nagar','dayitv','nagar','prant','vibhag','jila']

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
