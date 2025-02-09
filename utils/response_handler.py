from typing import Any, TypeVar, Generic
from rest_framework.response import Response
from rest_framework import status

T = TypeVar("T")


class ResponseHandler:
    @staticmethod
    def success(data: Any, status_code: int = status.HTTP_200_OK) -> Response:
        """
        Creates a success response with standardized format

        Args:
            data: The response data
            status_code: HTTP status code (default 200)
        """
        return Response({"status": "success", "body": data}, status=status_code)

    @staticmethod
    def error(message: Any, status_code: int = status.HTTP_400_BAD_REQUEST) -> Response:
        """
        Creates an error response with standardized format

        Args:
            message: Error message or details
            status_code: HTTP status code (default 400)
        """
        return Response({"status": "error", "body": message}, status=status_code)
