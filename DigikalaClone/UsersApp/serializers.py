from rest_framework import serializers
from django.db.models import Q
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_admin', 'is_active', 'id', 'password', ]

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(label=_("PhoneNumber"),)
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
    )
     
    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if phone_number and password:
            user = authenticate(request=self.context.get('request'),
                                username=phone_number, password=password)

            if not user:
                msg = _('Phone number or password is incorrect')
                raise serializers.ValidationError({'error':msg}, code='authorization')
        else:
            msg = _('Phone number and password is required')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class RegisterSerializer(serializers.Serializer):
    phone_number=serializers.CharField(max_length=20, required=True,)
    password=serializers.CharField(max_length=20, write_only=True, required=True,)
    password2=serializers.CharField(max_length=20, write_only=True, required=True,)
   

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'error':'Passwords are not matched'})
        if User.objects.filter(phone_number=data['phone_number']).count() == 1:
            raise serializers.ValidationError({'error':'This Phone number is already in used'})
        
        return super().validate(data)
    
    def create(self, validated_data):
        validated_data.pop('password2')
        
        user = User.objects.create_user(**validated_data)
        
        return user
