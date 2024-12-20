from rest_framework.exceptions import AuthenticationFailed
from ..social_auth.register import register_social_user
from rest_framework import serializers
from ..social_auth import google, facebook
import os


class GoogleSocialAuthSerializser(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired, Please try again.'
            )
        if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):
            raise AuthenticationFailed('oops who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'
        return register_social_user(
            provider=provider, user_id=user_id, email=email, name=name
        )


class FacebookSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = facebook.Facebook.validate(auth_token)

        try:
            user_id = user_data['id']
            email = user_data['email']
            name = user_data['name']
            provider = 'facebook'
            return register_social_user(
                provider=provider,
                user_id=user_id,
                email=email,
                name=name
            )
        except Exception as identifier:
            raise serializers.ValidationError(
                'The token is invalid or expired, Please try again.'
            )