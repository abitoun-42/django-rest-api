from rest_framework import generics
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import renderers

from django.contrib.auth.models import User

# from products.permissions import IsOwnerOrReadOnly add if we want a owner permissions
from products.serializers import UserSerializer
from products.models import Product
from products.serializers import ProductSerializer


class ProductHighlight(generics.GenericAPIView):
    queryset = Product.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *argv, **kwargs):
        product = self.get_object()
        return Response(product.highlighted)

class ProductList(generics.ListCreateAPIView):
    """
    List all code products, or create a new product.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()
        

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code product.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserList(generics.ListAPIView):
    """
    List all user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    """
    Root of api
    """
    return Response({
        'users' : reverse('user-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'token': reverse('token_obtain_pair', request=request, format=format),
        'refresh_token': reverse('token_refresh', request=request, format=format),
    })