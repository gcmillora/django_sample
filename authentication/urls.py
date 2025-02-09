from django.urls import path
from .views import (
    AuthenticationRegisterView,
    AuthenticationTokenView,
    AuthenticationRefreshTokenView,
    AuthenticationRevokeTokenView,
)

urlpatterns = [
    path("register/", AuthenticationRegisterView.as_view()),
    path("token/", AuthenticationTokenView.as_view()),
    path("refresh/", AuthenticationRefreshTokenView.as_view()),
    path("revoke/", AuthenticationRevokeTokenView.as_view()),
]
