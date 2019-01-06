from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from authentication.views import SignUp, SignUpAPIView

router = routers.DefaultRouter()
router.register('', SignUpAPIView, base_name='api-signup')

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('auth/signup/', include(router.urls)),
    path('auth/login/', obtain_jwt_token),
]
