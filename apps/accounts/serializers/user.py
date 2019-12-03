from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from apps.accounts.models import User
from sms.utils import get_validation_code


class UserSerializer(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    password = serializers.CharField(write_only=True, min_length=6)
    avatar = VersatileImageFieldSerializer(required=False, sizes='user_picture')
    
    class Meta:
        model = User
        fields = ('pk', 'phone_number', 'password', 'first_name', 'avatar')

    # def validate_email(self, email):
    #     if self.instance.email != email:
    #         # send verification email
    #         pass
    #     return email

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.username = user.uuid
        user.token = get_validation_code()
        user.save(update_fields=['username'])
        return user




