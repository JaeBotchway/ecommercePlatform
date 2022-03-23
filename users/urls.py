from django.urls import path
from .views import CreateUser, LogoutView, ProductView


urlpatterns = [
    path('register/', CreateUser.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('product/', ProductView.as_view(), name='product'),
    
]