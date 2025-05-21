# from rest_framework import serializers
# from .models import Login

# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Login
#         fields = ['email', 'password']

from rest_framework import serializers
from .models import Login

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['email', 'password']

    def create(self, validated_data):
        from django.contrib.auth.hashers import make_password
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'category', 'name']
from .models import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
     class Meta:
         model = Customer
         fields = ['customer_id', 'customer_name', 'phone_number', 'email_id', 'permanent_address']

from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'




