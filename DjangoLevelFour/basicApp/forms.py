from django import forms
from django.contrib.auth.models import User
from basicApp.models import UserInfoModel



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfoModel
        fields = ('portfolio_site','profile_pic')
