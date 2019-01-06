"""SocialNetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='TradeCore - Social Network')

urlpatterns = [
    path('', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('post.urls')),
    path('docs/', schema_view),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.login_template = 'login.html'
admin.site.index_title = 'TradeCore'
admin.site.site_title = 'Social Network'
admin.site.site_header = 'Social Network'
