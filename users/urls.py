from django.urls import path
from .views import CreateUser, LogoutView


urlpatterns = [
    path('register/', CreateUser.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),

    
]