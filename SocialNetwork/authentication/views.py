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
    SignUp API allows user to signup into the application using email and password.
    Once, you are signed up, Please proceed to login or session login.
    """
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    http_method_names = [
        'post',
    ]
    permission_classes = (AllowAny, )
