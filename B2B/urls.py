"""B2B URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from B2B_App import admin_urls, user_urls, farmer_urls
from B2B_App.views import IndexView, Login, Registration, farmer_reg

urlpatterns = [
    path('admin/', admin_urls.urls()),
    path('user/', user_urls.urls()),
    path('farmer/', farmer_urls.urls()),
    path('',IndexView.as_view()),
    path('User_Registration',Registration.as_view()),
    path('farmer_reg',farmer_reg.as_view()),
    path('login',Login.as_view())
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)