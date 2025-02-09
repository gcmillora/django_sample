from rest_framework import serializers
from application.models import CustomUser


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        if validated_data["password"] != validated_data["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        # Remove confirm_password from the data since we don't want to save it
        validated_data.pop("confirm_password")
        user = CustomUser.objects.create_user(
            email=validated_data["email"], password=validated_data["password"]
        )
        return user

    class Meta:
        model = CustomUser
        fields = ("id", "email", "password", "confirm_password")
        extra_kwargs = {
            "password": {"write_only": True},
            "confirm_password": {"write_only": True},
            "email": {"required": True},
        }
