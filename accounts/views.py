from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import AccountSerializer


User = get_user_model()

class AccountView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = AccountSerializer