from django import forms
from authentication.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    registration forms
    """
    # email = forms.EmailField()
    username = forms.CharField()
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name = forms.CharField(max_length=32, help_text='Last name')
    email = forms.EmailField(max_length=64, help_text='Enter a valid email address')
    company_name = forms.CharField(max_length=64, help_text="Company Name")
    company_reg = forms.CharField(max_length=64, help_text="Company Registration Number")
    company_number = forms.IntegerField(help_text="Company Tel")
    company_address = forms.CharField(max_length=128, help_text="Company Address")
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'company_name',
                  'company_address', 'company_number', 'company_reg', 'password1',
                  'password2']


class UserUpdateForm(forms.ModelForm):
    """
    forms to update the email and users name
    """
    username = forms.CharField()
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name = forms.CharField(max_length=32, help_text='Last name')
    email = forms.EmailField(max_length=64, help_text='Enter a valid email address')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'company_name',
                  'company_address', 'company_number', 'company_reg']


class ProfileUpdateForm(forms.ModelForm):
    """
    forms to update the image
    """

    class Meta:
        model = Profile
        fields = ['image']


# todo create an update password view and model