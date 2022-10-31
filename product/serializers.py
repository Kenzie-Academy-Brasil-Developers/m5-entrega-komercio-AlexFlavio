from rest_framework import serializers
from .models import Product
from account.serializers import AccountSerializer


class ProductSerializer(serializers.ModelSerializer):
    seller = AccountSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

        depth = 1

    ...


class ProductGeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["description", "price", "quantity", "is_active", "seller", "id"]

    ...
