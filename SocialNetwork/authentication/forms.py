import time

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from fullcontact import FullContact

from authentication.models import User

fullcontact = FullContact(settings.FULLCONTACT_API_KEY)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        response = fullcontact.query_emails(email)
        if response[email].get('status') in [202, 404]:
            raise forms.ValidationError('Email does not exist.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
