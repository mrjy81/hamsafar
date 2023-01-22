from django import forms
from django.forms import ValidationError
from account.models import Client, Driver, Phones
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class PassengerRegistrationForm(forms.Form):
    username = forms.CharField(label=_('نام کاربری'), max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'نام کاربری'}))
    password1 = forms.CharField(
        label=_('رمزعبور'), max_length=30, widget=forms.PasswordInput())
    password2 = forms.CharField(
        label=_('تکرار رمز عبور'), max_length=30, widget=forms.PasswordInput())
    phone = forms.CharField(label=_('تلفن همراه'), max_length=100, widget=forms.TextInput(
        attrs={'placeholder': '9227108903'}))

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password2 == password1:
            return password1
        else:
            raise ValidationError('عدم تطابق پسورد')

    def clean_phone(self):
        phone_number = self.cleaned_data['phone']
        if phone_number[0] == '0':
            phone_number = phone_number[1:]
        if len(phone_number) != 10:
            raise ValidationError('تعداد ارقام صحیح نمیباشد')
        if Phones.objects.filter(phone=phone_number).first():
            raise ValidationError('شماره قابل استفاده نمیباشد')
        return phone_number

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).first():
            raise ValidationError('نام کاربری در دسترس نیست')
        else:
            return username


class LoginForm(forms.Form):
    username = forms.CharField(label=_('نام کاربری'), max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'نام کاربری'}))
    password = forms.CharField(
        label=_('رمزعبور'), max_length=30, widget=forms.PasswordInput())


class DriverRegistrationForm(forms.Form):
    username = forms.CharField(label=_('نام کاربری'), max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'نام کاربری'}))
    password1 = forms.CharField(
        label=_('رمزعبور'), max_length=30, widget=forms.PasswordInput())
    password2 = forms.CharField(
        label=_('تکرار رمز عبور'), max_length=30, widget=forms.PasswordInput())
    phone = forms.CharField(label=_('تلفن همراه'), max_length=100, widget=forms.TextInput(
        attrs={'placeholder': '9227108903'}))

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password2 == password1:
            return password1
        else:
            raise ValidationError('عدم تطابق پسورد')

    def clean_phone(self):
        phone_number = self.cleaned_data['phone']
        if phone_number[0] == '0':
            phone_number = phone_number[1:]
        if len(phone_number) != 10:
            raise ValidationError('تعداد ارقام صحیح نمیباشد')
        if Phones.objects.filter(phone=phone_number).first():
            raise ValidationError('شماره قابل استفاده نمیباشد')
        return phone_number

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).first():
            raise ValidationError('نام کاربری در دسترس نیست')

        else:
            return username
