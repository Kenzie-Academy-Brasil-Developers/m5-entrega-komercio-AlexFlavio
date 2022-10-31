from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ["groups", "last_login", "email", "is_staff", "user_permissions"]
        extra_kwargs = {
            "password": {"write_only": True},
            "date_joined": {"read_only": True},
            "is_superuser": {"read_only": True},
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)
        ...

    ...

class AccountLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    ...


class AccountInactivatedSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "is_seller",
            "date_joined",
            "is_active",
            "is_superuser",
            "password",
        ]
        extra_kwargs = {"is_active": {"required": True}}
