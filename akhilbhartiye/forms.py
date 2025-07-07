
from django import forms
from akhilbhartiye.models import *

# Create your forms here.

class AkhilBhartiyaRegistrationForm(forms.ModelForm):
    class Meta:
        model = AkhilBhartiyaRegistration
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        # Replace empty strings with None (null)
        for field, value in cleaned_data.items():
            if isinstance(value, str) and value.strip() == "":
                cleaned_data[field] = None

        return cleaned_data

    # def clean(self):
    #     cleaned_data = super().clean()
    #     for key, value in cleaned_data.items():
    #         if value == "":
    #             cleaned_data[key] = None
    #     return cleaned_data