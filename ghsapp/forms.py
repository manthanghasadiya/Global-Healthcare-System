from django import forms
from django.contrib.auth.models import User
from .models import userInfo, doctorInfo, Appointment


class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name']


class userInfoForm(forms.ModelForm):
    class Meta():
        model = userInfo
        fields = ['mobile_number', 'profile_pic', 'dob', 'gender']


class doctorInfoForm(forms.ModelForm):
    class Meta():
        model = doctorInfo
        fields = ['mobile_number', 'profile_pic', 'hospital_name',
                  'degree_type', 'specialities_type', 'dob', 'gender']
