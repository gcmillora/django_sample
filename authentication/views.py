from rest_framework.views import APIView
from rest_framework import status
from authentication.serializers import CreateUserSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from utils.response_handler import ResponseHandler
import requests
import os
from typing import Any, TypeVar, Generic
from dotenv import load_dotenv

T = TypeVar("T")


def create_response(status_message: str, body: Any) -> dict:
    return {"status": status_message, "body": body}


load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Update the token URLs to use the correct path
TOKEN_URL = os.getenv("API_URL") + "/o/token/"
REVOKE_TOKEN_URL = os.getenv("API_URL") + "/o/revoke_token/"


class AuthenticationRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            r = requests.post(
                TOKEN_URL,
                data={
                    "grant_type": "password",
                    "username": request.data["email"],
                    "password": request.data["password"],
                    "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET,
                },
            )
            return ResponseHandler.success(r.json())
        return ResponseHandler.error(serializer.errors)


class AuthenticationTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        req = requests.post(
            TOKEN_URL,
            data={
                "grant_type": "password",
                "username": request.data["email"],
                "password": request.data["password"],
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            },
        )
        return ResponseHandler.success(req.json())


class AuthenticationRefreshTokenView(APIView):
    @permission_classes([AllowAny])
    def post(self, request):
        req = requests.post(
            TOKEN_URL,
            data={
                "grant_type": "refresh_token",
                "refresh_token": request.data["refresh_token"],
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            },
        )
        return ResponseHandler.success(req.json())


class AuthenticationRevokeTokenView(APIView):
    def post(self, request):
        req = requests.post(
            REVOKE_TOKEN_URL,
            data={
                "token": request.data["token"],
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            },
        )

        if req.status_code == requests.codes.ok:
            return ResponseHandler.success({"message": "Token revoked successfully"})
        return ResponseHandler.error(req.json(), status_code=req.status_code)
