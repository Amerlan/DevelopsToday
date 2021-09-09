from django.urls import path
from .views import LoginApi, RegisterApi, LogoutApi


urlpatterns = [
    path('signup/', RegisterApi.as_view(), name='login'),
    path('logout/', LogoutApi.as_view(), name='login'),
    path('login/', LoginApi.as_view(), name='login'),
]
