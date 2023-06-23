import logging

from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from result import Err

from applications.user.models import User
from applications.user.services.commands import user_register

logger = logging.getLogger(__name__)


class UserRegisterApi(APIView):
    class InputRegisterSerializer(serializers.Serializer):
        first_name = serializers.CharField(required=True)
        last_name = serializers.CharField(required=True)
        username = serializers.CharField(required=True)
        password = serializers.CharField(required=True)
        password2 = serializers.CharField(required=True)

        def validate_username(self, username):
            if User.objects.filter(username__exact=username).exists():
                raise serializers.ValidationError("username Already Taken")
            return username

        def validate(self, attrs):
            if not attrs.get("password") or not attrs.get("password2"):
                raise serializers.ValidationError("Please fill password and password2")

            if attrs.get("password") != attrs.get("password2"):
                raise serializers.ValidationError("password2 is not equal to password")
            return attrs

    class OutputRegisterSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ("id", "username", "first_name", "last_name")

    @extend_schema(request=InputRegisterSerializer, responses=OutputRegisterSerializer)
    def post(self, request):
        serializer = self.InputRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = user_register(
            username=data["username"], password=data["password"], first_name=data["first_name"],
            last_name=data["last_name"]
        )
        if isinstance(user, Err):
            logger.error(user.err())

            return Response(
                f"Database Error {user.err()}",
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(self.OutputRegisterSerializer(user.value, context={"request": request}).data)
