from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken
import jwt
from django.conf import settings

User = get_user_model()

# 회원가입 serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'nickname')
        extra_kwargs = {
            'username': {'required': True},
            'password': {'write_only': True, 'required': True},
            'nickname': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        return {
            "username": instance.username,
            "nickname": instance.nickname
        }

# 로그인 serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )
        if not user:
            raise serializers.ValidationError({
                "error": {
                    "code": "INVALID_CREDENTIALS",
                    "message": "아이디 또는 비밀번호가 올바르지 않습니다."
                }
            })
        
        token = AccessToken.for_user(user)
        return {
            "token": str(token)
        }

# 토큰 검증 serializer
class TokenVerifySerializer(serializers.Serializer):
    token = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def validate(self, attrs):
        token = attrs.get('token', '')

        if not token:
            raise serializers.ValidationError({
                "error": {
                    "code": "TOKEN_NOT_FOUND",
                    "message": "토큰이 없습니다."
                }
            })
            
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            return {"user": user}

        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError({
                "error": {
                    "code": "TOKEN_EXPIRED",
                    "message": "토큰이 만료되었습니다."
                }
            })
        except (jwt.InvalidTokenError, User.DoesNotExist):
            raise serializers.ValidationError({
                "error": {
                    "code": "INVALID_TOKEN",
                    "message": "토큰이 유효하지 않습니다."
                }
            })
