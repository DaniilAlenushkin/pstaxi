from django import forms
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm, PasswordChangeForm,
                                       PasswordResetForm, SetPasswordForm)
from accounts.models import Profile
from utils.forms import update_fields_widget
from allauth.account.forms import LoginForm


class CustomUserCreationForm(UserCreationForm):
    # TODO разобраться с записью емейла
    # email = forms.EmailField(max_length=64, help_text='Введите свой email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        update_fields_widget(self, ('username', 'password1', 'password2'), 'form-control')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        update_fields_widget(self, ('phone',), 'form-control')


class CustomAuthenticationForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        update_fields_widget(self, ('login', 'password'), 'form-control')


class CustomPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        update_fields_widget(self, ('old_password', 'new_password1', 'new_password2'), 'form-control')


class CustomPasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        update_fields_widget(self, ('email',), 'form-control')


class CustomSetPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        update_fields_widget(self, ('new_password1', 'new_password2',), 'form-control')
