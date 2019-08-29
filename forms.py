from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

'''class SearchForm(forms.ModelForm):

    search = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'style': 'max-width: 10em'}),
        required=True,
    )
'''
class SignUpForm(UserCreationForm):

    email = forms.EmailField(label="Email Address")

    class Meta:

        model = User
        fields = ("email","username","password1","password2")

