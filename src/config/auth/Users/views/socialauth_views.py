from ..serializers.socialauth_serializers import GoogleSocialAuthSerializser, FacebookSocialAuthSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


class GoogleSocialAuthView(GenericAPIView):
    serializer_class = GoogleSocialAuthSerializser

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)

class FacebookSocialAuthView(GenericAPIView):
    serializer_class = FacebookSocialAuthSerializer

    def post(self,request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)