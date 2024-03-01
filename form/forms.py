from django import forms

from django.core.validators import RegexValidator


class MyForm(forms.Form):
    name = forms.CharField(max_length=30, label='Name', widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    age = forms.IntegerField(required=False, label='Age')
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], label='Gender')
    birthday = forms.DateField(required=False, label='Birthday')
    address = forms.CharField(max_length=100, label='Address')
    city = forms.CharField(max_length=30, label='City')
    state = forms.CharField(max_length=30, label='State')
    country = forms.CharField(max_length=30, label='Country')
    phone = forms.CharField(max_length=10, validators=[RegexValidator(r'^\+?1?\d{9,13}$',
                                                                      message='Phone number must be entered in the '
                                                                              "format '+123456789'."
                                                                              'Up to 15 digits'
                                                                              'allowed.')], label='Phone')


