from django.conf.urls import url
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
from .views import LoginView, LogoutView, UsernameValidationView, EmailValidationView, \
    VerificationView, RegistrationView

urlpatterns = [
    # authentication, validations, login, logout paths
    path('register/', RegistrationView.as_view(), name='register-page'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),name='validate_email'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         views.activate,name='activate'),
    path('activate/<uidb64>/<token>',VerificationView.as_view(), name='activate'),

    path('redirect/', views.redirectpages, name="redirect"),
    path('login/', LoginView.as_view(), name="login"),
    path('user/<str:username>', views.profile, name='profile-page'),
    path('logout/', LogoutView.as_view(), name="logout"),

]