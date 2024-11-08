# forms.py
from django import forms

from .models import BuySkiPass, ReplenishmentOfBalanceSkiPass, PeopleReservationCottage, CottageReservation


class DateForm(forms.Form):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'base-date-input', 'placeholder': 'Выберите дату'})
    )
class ReplenishmentForm(forms.ModelForm):
    class Meta:
        model = ReplenishmentOfBalanceSkiPass
        fields = ['tarif', 'phone', 'email', 'numberCard', 'summ']
        widgets = {
            'tarif': forms.TextInput(attrs={'placeholder': 'Тариф'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Электронная почта'}),
            'numberCard': forms.TextInput(attrs={'placeholder': 'Номер карты'}),
            'summ': forms.NumberInput(attrs={'placeholder': 'Сумма'}),
        }

class BuySkiPassForm(forms.ModelForm):
    class Meta:
        model = BuySkiPass
        fields = ['type', 'price', 'fullName', 'phone', 'email']
        widgets = {
            'type': forms.NumberInput(attrs={'placeholder': 'Тип'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Цена'}),
            'fullName': forms.TextInput(attrs={'placeholder': 'ФИО'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Электронная почта'}),
        }

class CottageReservationForm(forms.ModelForm):
    class Meta:
        model = CottageReservation
        fields = ['dateFrom', 'dateTo', 'cottage']
        widgets = {
            'dateFrom': forms.DateInput(attrs={'type': 'date'}),
            'dateTo': forms.DateInput(attrs={'type': 'date'}),
        }

# Форма для добавления людей
class PeopleReservationForm(forms.ModelForm):
    class Meta:
        model = PeopleReservationCottage
        fields = ['fullName']