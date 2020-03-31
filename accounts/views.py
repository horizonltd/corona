from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from accounts.models import User, TypeOfMembership
from accounts.serializers import UserSerializer, TypeOfMembershipSerializer
# Also add these imports
from accounts.permissions import IsLoggedInUserOrAdmin, IsAdminUser
# Also add these imports
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated





class TypeOfMembershipViewSet(viewsets.ModelViewSet):
    queryset = TypeOfMembership.objects.all()
    serializer_class = TypeOfMembershipSerializer
    #authentication_classes = (TokenAuthentication, )
    #permission_classes = (IsAuthenticated, )

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]