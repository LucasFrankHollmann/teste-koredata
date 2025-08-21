from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import User

class UserSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(region="BR")

    class Meta:
        model = User
        fields = '__all__'
