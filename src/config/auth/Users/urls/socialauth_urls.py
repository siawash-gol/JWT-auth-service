from .views.login_views import (LoginView, LogoutView, RequestResetPasswordView,
                                CheckRequestResetPasswordView, SetNewPasswordView)
from .views.socialauth_views import GoogleSocialAuthView, FacebookSocialAuthView
from .views.register_views import RegisterView, VerifyEmailView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path


urlpatterns = [
    # social auth
    path('social/auth/google', GoogleSocialAuthView.as_view(), name='social_google'),
    path('social/auth/facebook', FacebookSocialAuthView.as_view(), name='social_facebook'),
]
