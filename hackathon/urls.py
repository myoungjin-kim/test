"""
URL configuration for hackathon project.

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
from django.urls import path
import hackathonapp.views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('list_edit', hackathonapp.views.list_edit, name="list_edit"), # 여기서는 안붙여야 작동되는데??
    path('re_home/', hackathonapp.views.re_home, name="re_home"),
    path('list_db/', hackathonapp.views.list_db, name="list_db"), #????
    path('list/', hackathonapp.views.list,name="list"),
    path('admin', admin.site.urls),
    path('', hackathonapp.views.home,name='home'),#처음 접속했을때 로그인하는 기본화면
    path('signup/', hackathonapp.views.signup,name='join'),#회원가입화면
    path('login', auth_views.LoginView.as_view(template_name='login.html'),name='login'),#0
    path('main/', hackathonapp.views.main,name='main'),#로그인 되었을때 화면 #0
    path('recommend/', hackathonapp.views.recommend, name="recommend"),
    path('update', hackathonapp.views.update, name="update"),
]
# 이는 Django의 URL 설계 철학과 관련이 있습니다.
#
# 예를 들어, 'about/'와 '/about' 사이에는 큰 차이가 있습니다.
#
# 'about/': 이 패턴은 www.yourwebsite.com/about/를 의미합니다.
# '/about': Django에서는 이런 식으로 시작 슬래시를 사용하지 않습니다. 만약 사용하게 되면 예상치 못한 동작을 할 수 있습니다.
# 따라서 항상 경로 문자열을 작성할 때 시작하는 슬래시(/) 없이 작성해야 합니다. 또한, Django에서는 URL 끝에 슬래시(/)를 붙이는 것을 관례로 하고
# 있으므로 (트레일링 슬래시), 가능하면 URL 끝에 슬래시를 포함하는 것이 좋습니다.
#
# 그러나 만약 특별히 URL 뒤에 슬래시 없이 정의하고 싶다면 Django 설정 중 APPEND_SLASH = False 로 설정하여 자동으로 뒤에 붙는 슬래시 기능을 꺼줄 수도 있습니다.