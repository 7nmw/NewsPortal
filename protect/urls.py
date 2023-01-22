from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='protect'), #http://127.0.0.1:8000/index
]