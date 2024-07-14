from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.serializers import UserSerializer


class User_API(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (AllowAny,)
        else:
            self.permission_classes = (IsAuthenticated,)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(password=make_password(serializer.save().password))

    def perform_update(self, serializer):
        serializer.save(password=make_password(serializer.save().password))
