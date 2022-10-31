from rest_framework import generics
from rest_framework.views import Request, Response, APIView, status
from .models import Account
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import (
    AccountSerializer,
    AccountInactivatedSerializer,
    AccountLoginSerializer,
)
from .permissions import IsAccountOwner, OnlyAdmin
from rest_framework.authentication import TokenAuthentication


class AccountView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class AccountListView(generics.ListAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def get_queryset(self):
        num = self.kwargs["num"]

        return self.queryset.order_by("-date_joined")[0:num]
        ...


class AccountUpdateView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        request.data.pop("is_active", None)
        return self.update(request, *args, **kwargs)


class AccountDeleteView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OnlyAdmin]

    serializer_class = AccountInactivatedSerializer
    queryset = Account.objects.all()


class LoginView(APIView):

    queryset = Account
    serializer_class = AccountLoginSerializer

    def post(self, request: Request) -> Response:
        serializer = AccountLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if not user:
            return Response(
                {"detail": "invalid username or password"}, status.HTTP_403_FORBIDDEN
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})
        ...

    ...
