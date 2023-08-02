from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={ 'placeholder':'Username'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={ 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={ 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={ 'placeholder':'Last Name'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={ 'placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     'username': UserCreationForm.default_widget['username'],
        #     'email': UserCreationForm.default_widget['email'],
        # }
        labels = {
            'username': 'Username',
            'email': 'Email',
        }
        help_texts = {
            'username': 'Enter a username',
            'email': 'Enter an email address',
        }
        error_messages = {
            'username': {
                'unique': 'This username is already in use.',
            },
            'email': {
                'unique': 'This email address is already in use.',
            },
        }

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            self.fields['username'].label = ''
            self.fields['username'].widget.attrs['placeholder'] = 'Username'
            self.fields['username'].help_text = '<span class=""><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].label = ''
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
            
            self.fields['password2'].label = ''
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].help_text = '<span class=""><small>Enter the same password as before, for verification.</small></span>'	


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'', 'placeholder':'Username'}))
    password = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'', 'placeholder':'Password'}))
    # remember_me = forms.BooleanField(label="Remember Me", required=False)

    class Meta:
        model = User