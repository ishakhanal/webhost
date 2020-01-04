from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from users.models import Profile

class RegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class EditProfileForm(ModelForm):
         class Meta:
         	model = User
         	fields = ('email','first_name','last_name')

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'location', 'phone_number', 'birth_date', 'citizenship_number', 'image', 'citizenship_image') #Note that we didn't mention user field here.