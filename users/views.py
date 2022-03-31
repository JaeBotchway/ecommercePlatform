from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistrationSerializer, ProductSerializer
from .models import Product




# Create your views here.

class CreateUser(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            # print(refresh_token)
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.order_by('-timestamp')
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    
    
class DetailProductView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    model = Product
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)



