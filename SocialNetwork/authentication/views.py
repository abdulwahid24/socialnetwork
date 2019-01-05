from django.urls import reverse_lazy
from django.views import generic

from authentication.forms import SignUpForm


class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('admin:login')
    template_name = 'signup.html'
