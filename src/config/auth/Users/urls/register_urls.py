from .views.register_views import RegisterView, VerifyEmailView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

urlpatterns = [
    # registration
    path('register/', RegisterView.as_view(), name='register'),
    path('email-verify/', VerifyEmailView.as_view(), name='email_verify'),
]
