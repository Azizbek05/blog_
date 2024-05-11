from django.urls import path

from .views import register, log_in,log_out, verify

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('verify/', verify, name='verify')

]