from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ['is_active']
        exclude = ('is_staff', 'is_superuser', 'groups', 'user_permissions')
