from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserInformations


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    
    def save(self, commit = True):
        user = super().save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active=False

        if commit:
            user.save()
        return user

class UserInformationForm(forms.ModelForm):
    company_choice = (('1', '48 Forty Solutions'),('2', '4 Earch Farms'),('3', 'A & A Organic Farms'),('4', 'A-1 Cold Storage'))
    company = forms.ChoiceField(choices = company_choice)
    role_choice = (('1', 'Produce Industry Employee'),('2', 'Retail Employee'),('3', '3rd Party Marketer or Service'),('4', 'Consumer'))
    role = forms.ChoiceField(choices = role_choice)

    class Meta:
        model = UserInformations
        fields = ('company', 'role' , 'title')