from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('page/', home2, name='home2'),
    path('send-email', send_email, name='send_email'),
]