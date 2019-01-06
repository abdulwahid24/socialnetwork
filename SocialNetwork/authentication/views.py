from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from authentication.forms import SignUpForm
from authentication.models import User
from authentication.serializers import SignUpSerializer


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('admin:login')
    template_name = 'signup.html'


class SignUpAPIView(ModelViewSet):
    """
    API View that returns a refreshed token (with new expiration) based on
    existing token

    If 'orig_iat' field (original issued-at-time) is found, will first check
    if it's within expiration window, then copy it to the new token
    """
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    http_method_names = [
        'post',
    ]
    permission_classes = (AllowAny, )
