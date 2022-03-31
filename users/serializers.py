from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Product 

class RegistrationSerializer(serializers.ModelSerializer):
    
    password1 = serializers.CharField(max_length=200,min_length =6, write_only=True)
    password2 = serializers.CharField(max_length=200,min_length =6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


    def validate(self,data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Password does not match")
        return data

    def create(self, validated_data, *args, **kwargs):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )    
        user.set_password(validated_data['password1'])
        user.save()

        return user
    

    




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'description', 'price', 'discount', 'image1', 'image2','image3', 'category', 'timestamp']
        ordering = ('-timestamp')


