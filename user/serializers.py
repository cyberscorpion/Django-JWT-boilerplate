from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _

from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER
#class UserCreateSerializer(ModelSerializer):
#    class Meta:
#        model = User
#        fields = [
#            'profile_photo',
#            'email',
#            'username',
#            'name',
#            'platform',
#        ]
class UserCreateSerializer(ModelSerializer):
#    password = serializers.CharField(source='model_method')
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields=[
            'profile_photo',
            'username',
            'password',
            'email',
            'name',
            'platform',
            'phone',
            'token',
        ]
        extra_kwargs = {"password":{"write_only":True}}


    def get_token(self,user):
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise serializers.ValidationError(msg)
            payload = jwt_payload_handler(user)
            return jwt_encode_handler(payload)
        else:
            msg = _('Unable to log in.')
            raise serializers.ValidationError(msg)
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
#        username=validated_data['username']
#        email=validated_data['email']
#        password=validated_data['password']
#        name=validated_data['name']
#        platform=validated_data['platform']
#        phone=validated_data['phone']
#        user_obj= User(
#                username=username,
#                email=email,
#                name=name,
#                platform=platform,
#                phone=phone
#        )
#        user_obj.set_password(password)
#        user_obj.is_active = False
#        user_obj.save()

#        token_obj = UserToken.objects.create(user = user_obj, token = uuid.uuid1(), token_type =1)
#        current_site = get_current_site(self.context['request'])
        user.token = "dfd"
#        user.token = serializer.object.get('token')
        return user
#        return validated_data
    
    def validate(self,data):
        username=data['username']
        email=data['email']
#        first_name=data['first_name']
#        last_name=data['last_name']
        
        user_un= User.objects.filter(username=username)
        user_em= User.objects.filter(email=email)
        if user_un.exists():
            raise ValidationError("Username already exits")
        if user_em.exists():
            raise ValidationError("Email already exits")
        return data
    
class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields=[
            'profile_photo',
            'username',
            'email',
            'name',
            'platform',
            'phone',
        ]