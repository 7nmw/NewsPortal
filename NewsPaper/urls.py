"""NewsPaper URL Configuration

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
from news.views import PostSearch
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from protect.views import IndexView

urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   path('news/', include('news.urls')),
   path('article/', include('news.urls')),
   path('news/search/', PostSearch.as_view(), name='search'),
   path('', include('protect.urls')),
   path('sign/', include('sign.urls')),
   path('accounts/', include('allauth.urls')), #http://127.0.0.1:8000/accounts/login/
   path('subscribe/', include('news.urls')), #http://127.0.0.1:8000/subscribe/
   path('__debug__/', include('debug_toolbar.urls')),
   path('i18n/', include('django.conf.urls.i18n')), # подключаем встроенные эндопинты для работы с локализацией
]
