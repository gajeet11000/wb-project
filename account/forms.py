from django.contrib.auth.models import User

from django.contrib.auth import forms as auth_forms

from django import forms
from django.forms import widgets

from django.db.models import Q
from django.contrib import auth

class CreateUserForm(auth_forms.UserCreationForm):
    email = forms.EmailField(
        required=True,
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(auth_forms.AuthenticationForm):
    username = forms.CharField(
        required=True,
        max_length=150, 
        label='Username or Email',
        widget=widgets.TextInput(),
    )
    password = forms.CharField(
        required=True,
        label="Password",
        widget=widgets.PasswordInput()
    )
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        invalid = False
        
        if username and password:
            user = User.objects.filter(
                (Q(username=username) | Q(email=username))
            ).first()
            
            if user is not None:
                self.user_cache = auth.authenticate(username=user.username, password=password)
                
                if self.user_cache is not None:
                    self.confirm_login_allowed(self.user_cache)
                    self.cleaned_data['user'] = self.user_cache
                else:
                    invalid = True
            else:
                invalid = True
        else:
            invalid = True
            
        if invalid:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name},
            )

        return self.cleaned_data