from rest_framework import serializers
from products.models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    # highlight = serializers.HyperlinkedIdentityField(view_name='product-highlight', format='html')
    class Meta:
        model = Product
        fields = ['id', 'title', 'img',
                  'price','company', 'info', 'inCart', 'count', 'total']

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username']
