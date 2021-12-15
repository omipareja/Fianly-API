from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from applications.users.api.serializers.UserSerializer import UserSerializer


class UserViewSet(viewsets.GenericViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    def get_permissions(self):
        if (self.action == 'list'):
            permission_classes = [IsAuthenticated]
        elif (self.action == 'create'):
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        """
        UserListEndPoint

            Header: Bearer token_access

            Response: [{
                        'user_name':'User_name',
                        'user_lastname:'User Last Name'
                      }]
        """
        try:
            serializer = self.serializer_class(self.get_queryset(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error_message': 'Error al cargar los datos'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        """
         UserListEndPoint

             Header: Bearer token_access

             Body: {
                        'username':'Username',
                        'email':'email',
                        'first_name':'first_name',
                        'password': 'password'
                    }

             Response: {
                         'message':'Usuario Creado Con Exito'
                       }
         """
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Creacion de usuario Exitosa'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
