from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
# from home.serializers import StudentSerializer
from account.models import User
from home.models import Student

from django.utils.encoding import force_str, DjangoUnicodeDecodeError


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=68, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'user_type', 'full_name', 'username', 'date_of_birth', 'gender','email','password', 'password2',)
        # fields = ('user_type','full_name','username','date_of_birth','gender','objects','groups','password', 'password2')
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError({'success': False, 'message': 'Password did not match, please try again'})
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)



class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=68, write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    def get_tokens(self, obj):
        username = obj.get('username')
        tokens = User.objects.get(username=username).tokens
        return tokens

    class Meta:
        model = User
        fields = ('username', 'tokens', 'password')

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed({
                'message': 'username or password is not correct'
            })
        if not user.is_active:
            raise AuthenticationFailed({
                'message': 'Account disabled'
            })

        data = {
            'username': user.username,
        }
        return data


class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('username',)


class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name',)


class AccountOwnImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('image',)


class SetNewPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=64, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=64, write_only=True)
    uidb64 = serializers.CharField(max_length=68, required=True)
    token = serializers.CharField(max_length=555, required=True)

    class Meta:
        model = User
        fields = ('password', 'password2', 'uidb64', 'token')

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        uidb64 = attrs.get('uidb64')
        token = attrs.get('token')
        _id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.filter(id=_id).first()
        current_password = user.password
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise AuthenticationFailed({'success': False, 'message': 'The token is not valid'})
        if password != password2:
            raise serializers.ValidationError({
                'success': False, 'message': 'Password did not match, please try again'
            })

        if check_password(password, current_password):
            raise serializers.ValidationError(
                {'success': False, 'message': 'New password should not similar to current password'})

        user.set_password(password)
        user.save()
        return attrs


class ChangeNewPasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(min_length=6, max_length=64, write_only=True)
    password = serializers.CharField(min_length=6, max_length=64, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=64, write_only=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        old_password = attrs.get('old_password')
        password = attrs.get('password')
        password2 = attrs.get('password2')
        request = self.context.get('request')
        user = request.user
        if not user.check_password(old_password):
            print(55555555)
            raise serializers.ValidationError(
                {'success': False, 'message': 'Old password did not match, please try again new'})

        if password != password2:
            print(321)
            raise serializers.ValidationError(
                {'success': False, 'message': 'Password did not match, please try again new'})

        user.set_password(password)
        user.save()
        return attrs
