
from django import forms
from .models import *

# Create your forms here.

class GhoshVargRegisterForm(forms.ModelForm):
    class Meta:
        model = GhoshVargRegister
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        for key, value in cleaned_data.items():
            if value == "":
                cleaned_data[key] = None
        return cleaned_data