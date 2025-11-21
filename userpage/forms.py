from django import forms
from .models import UserRegister
from datetime import date

class UserForm(forms.ModelForm):
    class Meta:
        model = UserRegister
        fields = ['name', 'age', 'email', 'is_active', 'dob', 'gender']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_dob(self):
        dob = self.cleaned_data.get("dob")

        if dob and dob > date.today():
            raise forms.ValidationError("Date of birth cannot be a future date.")

        return dob
