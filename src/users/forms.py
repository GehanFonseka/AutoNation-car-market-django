from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from localflavor.us.forms import USZipCodeField
from .widgets import CustomPictureImageFieldWidget
from .models import Location, Profile



class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password1(self):
        # Skip unwanted validations for password (if there is a password field)
        password = self.cleaned_data.get('password1')
        if password and len(password) < 8:
            raise forms.ValidationError("Your password must contain at least 8 characters.")
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields must match.")
        return password2


class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    bio = forms.TextInput()

    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number')


class LocationForm(forms.ModelForm):

    address_1 = forms.CharField(required=True)
    

    class Meta:
        model = Location
        fields = {'address_1', 'address_2', 'city', 'state'}