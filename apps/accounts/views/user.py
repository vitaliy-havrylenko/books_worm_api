from rest_framework import viewsets, mixins
from apps.accounts.models import User
from apps.accounts.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



