from django.contrib.auth.forms import UserCreationForm

from authentication.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
