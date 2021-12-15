from rest_framework.response import Response
from rest_framework import status
from applications.users.api.serializers.LoginSerializer import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth import authenticate


class Login(APIView):

    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        """
         UserListEndPoint

             Header: Bearer token_access

             Body: {
                        'user':'Username',
                        'password': 'password'
                    }

             Response: {
                         'token':'token_for_access',
                         'user_name':'User_name'
                       }
         """
        received_json_data = request.data
        serializer = LoginSerializer(data=received_json_data)
        if serializer.is_valid():
            user = authenticate(
                username=received_json_data['user'],
                password=received_json_data['password']
            )

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'Token': str(refresh.access_token),
                    # 'Token_refresh':str(refresh),
                    'user_name': user.username
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error_message': 'Credenciales inválidas o usuario inexistente”'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error_message': 'Petición inválida'}, status=status.HTTP_400_BAD_REQUEST)
