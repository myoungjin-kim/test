"""
URL configuration for board project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

import hackathon.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hackathon.views.home,name='home'),#기본화면
    path('join/', hackathon.views.signup_view,name='join'),
    path('login/', hackathon.views.login,name='login'),
    path('main/', hackathon.views.main,name='main'),#로그인 되었을때 화면


    # path('',include('boardapp.urls')),
    # path('',include('album.urls')),


]
