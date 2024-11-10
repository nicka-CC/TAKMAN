# forms.py
from django import forms

from .models import BuySkiPass, ReplenishmentOfBalanceSkiPass, PeopleReservationCottage, CottageReservation, \
    ReservationInstrument, PeopleReservationInstrument, ReservationInstructor, PeopleReservationInstructor, \
    BuyCertificate


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
class InstrumentReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationInstrument
        fields = ['date', 'time', 'instructor', 'instrument', 'price']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
# Форма для добавления людей
class PeopleReservationInstrumrntForm(forms.ModelForm):
    class Meta:
        model = PeopleReservationInstrument
        fields = ['fullName']


class InstructorReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationInstructor
        fields = ['date', 'time', 'instructor', 'price']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
# Форма для добавления людей
class PeopleReservationInstructorForm(forms.ModelForm):
    class Meta:
        model = PeopleReservationInstructor
        fields = ['fullName']


class BuySertificateForm(forms.ModelForm):
    class Meta:
        model = BuyCertificate
        fields = ['fullNameBuyer', 'fullNameUses', 'phone', 'email', 'price']