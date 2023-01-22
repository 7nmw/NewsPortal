from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView
from .views import upgrade_me

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'), #http://127.0.0.1:8000/sign/login/
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'), #http://127.0.0.1:8000/sign/logout/
    path('signup/',
         BaseRegisterView.as_view(template_name='sign/signup.html'),
         name='signup'),  #http://127.0.0.1:8000/sign/signup/
    path('upgrade/', upgrade_me, name = 'upgrade')
]