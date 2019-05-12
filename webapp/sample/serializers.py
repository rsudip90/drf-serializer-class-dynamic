from rest_framework import serializers
from enumfields.drf.serializers import EnumSupportSerializerMixin

from .models import User, Company

class CompanySerializer(serializers.ModelSerializer):
    full_address = serializers.CharField(read_only=True)

    class Meta:
        model = Company
        fields = ("id", "name", "email", "phone", "full_address", "logo_url")

class CompanyDetailSerializer(serializers.ModelSerializer):
    full_address = serializers.CharField(read_only=True)

    class Meta:
        model = Company
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    company_details     = CompanySerializer(source="company", read_only=True)
    full_address        = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "company_details", "company", "full_address", )
        extra_kwargs = {
            'company': {'write_only': True},
        }

class UserDetailSerializer(EnumSupportSerializerMixin, serializers.ModelSerializer):
    company_details     = CompanySerializer(source="company", read_only=True)
    full_address        = serializers.CharField(read_only=True)

    class Meta:
        model = User
        exclude = ("password", "groups", "user_permissions", "date_joined", )
        extra_kwargs = {
            'company': {'write_only': True},
        }

