from django.urls import path, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from todo.views import UserRegistrationAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
]
