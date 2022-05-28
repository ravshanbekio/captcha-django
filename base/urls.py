from django.urls import path
from .views import register, home, login_user, logout

urlpatterns = [
    path('',home, name='home'),
    path('register/',register, name='register-view'),
    path('login/',login_user, name='login'),
    path('logout/',logout, name='logout')
]