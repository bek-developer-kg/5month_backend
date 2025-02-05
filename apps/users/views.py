from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.serializer import UserSerializer, UserRegisterSerializer
# Create your views here.

class UserAPIList(GenericViewSet,
                  mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated)

class UserAPIRegister(GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer