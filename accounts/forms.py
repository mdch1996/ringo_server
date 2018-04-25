from django import forms
from django.contrib.auth.models import User
from .models import Device


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        # print("------self-----", self)
        cd = self.cleaned_data
        # print("------cd-----", cd)
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class DeviceEditForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('raspberry_pi_code',)