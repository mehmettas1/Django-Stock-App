from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )
    password1 = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password1"
        )

    def validate(self, data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError(
                {"password": "Password must be same with above ! ..."}
            )
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password1')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )

class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)
    class Meta(TokenSerializer.Meta):
        fields = (
            "key",
            "user"
        )
