from django import forms


class LoginForm(forms.Form):
    # username       = forms.EmailField(label='Email')
    email       = forms.EmailField(label='Email')
    password    = forms.CharField(
        widget=forms.PasswordInput()
    )