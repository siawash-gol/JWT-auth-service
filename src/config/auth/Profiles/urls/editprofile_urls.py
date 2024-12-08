from .views.editprofile_view import EditProfileView, ChangePasswordView, SupportView
from django.urls import path

urlpatterns = [
    path('<slug:slug>/edit-profile', EditProfileView.as_view(), name='edit_profile'),
    path('<slug:slug>/change-password', ChangePasswordView.as_view(), name='change_password'),
    path('<slug:slug>/support', SupportView.as_view(), name='support'),
]
