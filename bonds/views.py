from bonds.models import Bond, Company
from bonds.serializers import UserSerializer, BondSerializer, CompanySerializer
from rest_framework import generics, permissions, renderers
from django.contrib.auth.models import User
from bonds.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'bonds': reverse('bond-list', request=request, format=format),
        'companies': reverse('company-list', request=request, format=format)
    })

class BondList(generics.ListCreateAPIView):
    queryset = Bond.objects.all()
    serializer_class = BondSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BondDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bond.objects.all()
    serializer_class = BondSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
