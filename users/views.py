from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer


class User_API(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer.save(password=make_password(serializer.save().password))

    def perform_update(self, serializer):
        serializer.save(password=make_password(serializer.save().password))
