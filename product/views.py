from urllib import request
from rest_framework import generics

from rest_framework.views import APIView

from .models import Product

from .serializers import ProductSerializer, ProductGeralSerializer
from .permissions import CustomPermission
from rest_framework.authentication import TokenAuthentication
from utils.mixins import CustomMixinSerializerByMethod


class ProductView(CustomMixinSerializerByMethod, generics.ListCreateAPIView):

    permission_classes = [CustomPermission]
    queryset = Product.objects.all()
    serializer_map = {
        'GET': ProductGeralSerializer,
        'POST': ProductSerializer,
    }

    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

    ...


class ProductDetailView(generics.RetrieveUpdateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomPermission]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    ...
