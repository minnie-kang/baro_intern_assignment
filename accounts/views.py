from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import serializers

from .serializers import RegisterSerializer, LoginSerializer, TokenVerifySerializer

User = get_user_model()

# 회원가입 view
class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    @extend_schema(
        summary="회원가입",
        request=RegisterSerializer,
        responses={
            201: OpenApiResponse(
                response=RegisterSerializer,
                description="회원가입 성공한 경우"
            ),
            400: OpenApiResponse(
                description="회원가입에 실패한 경우",
                response={
                    "type": "object",
                    "properties": {
                        "error": {
                            "type": "object",
                            "properties": {
                                "code": {"type": "string", "example": "USER_ALREADY_EXISTS"},
                                "message": {"type": "string", "example": "이미 가입된 사용자입니다."}
                            }
                        }
                    }
                }
            )
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# 로그인 view
class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    @extend_schema(
        summary="로그인",
        request=LoginSerializer,
        responses={
            200: OpenApiResponse(
                description="로그인 성공에 성공한 경우",
                response={
                    "type": "object",
                    "properties": {
                        "token": {"type": "string", "example": "eKDIkdfjoakIdkfjpekdkcjdkoIOdjOKJDFOlLDKFJKL"}
                    }
                },
            ),
            401: OpenApiResponse(
                description="로그인에 실패한 경우",
                response={
                    "type": "object",
                    "properties": {
                        "error": {
                            "type": "object",
                            "properties": {
                                "code": {"type": "string", "example": "INVALID_CREDENTIALS"},
                                "message": {"type": "string", "example": "아이디 또는 비밀번호가 올바르지 않습니다."}
                            }
                        }
                    }
                },
                
            )
        },
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


# 토큰 검증 view
class TokenVerifyView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = TokenVerifySerializer

    @extend_schema(
        summary="토큰 검증",
        request=TokenVerifySerializer,
        responses={
            200: OpenApiResponse(
                description="토큰이 유효한 경우",
                response={
                    "type": "object",
                    "properties": {
                        "message": {"type": "string", "example": "유효한 토큰입니다."}
                    }
                }
            ),
            401: OpenApiResponse(
                description="토큰이 유효하지 않은 경우",
                response={
                    "type": "object",
                    "properties": {
                        "error": {
                            "type": "object",
                            "properties": {
                                "code": {"type": "string"},
                                "message": {"type": "string"}
                            }
                        }
                    }
                }
            )
        },
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            return Response({"message": "유효한 토큰입니다."}, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            return Response(e.detail, status=status.HTTP_401_UNAUTHORIZED)
