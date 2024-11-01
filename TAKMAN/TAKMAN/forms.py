# forms.py
from django import forms

class DateForm(forms.Form):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'base-date-input', 'placeholder': 'Выберите дату'})
    )
