from .views.login_views import (LoginView, LogoutView, RequestResetPasswordView,
                                CheckRequestResetPasswordView, SetNewPasswordView)
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

urlpatterns = [
    # login
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password-reset-request/', RequestResetPasswordView.as_view(),
         name="request-reset-email"),
    path('password-reset-check/<str:uidb64>/<str:token>/',
         CheckRequestResetPasswordView.as_view(), name='password-reset-check'),
    path('password-reset-complete', SetNewPasswordView.as_view(),
         name='password-reset-complete'),
]
