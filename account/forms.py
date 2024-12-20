from django.contrib.auth.models import User

from django.contrib.auth import forms as auth_forms

class CreateUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
