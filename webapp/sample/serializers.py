from rest_framework import serializers
from enumfields.drf.serializers import EnumSupportSerializerMixin

from .models import User, Company

class UserBasicDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", )

class WhoDidSerializerMixin(serializers.BaseSerializer):
    """
    Replace `created_by`, `modified_by` details by detailed
    user basic info instead of user ID
    """
    def to_representation(self, instance):
        resp = super().to_representation(instance)

        # replace created_by field
        if "created_by" in resp and resp["created_by"] is not None:
            user = User.objects.filter(pk=resp["created_by"]).first()
            if user is not None:
                resp["created_by"] = UserBasicDetailSerializer(user).data
            else:
                resp["created_by"] = {}

        # replace modified_by field
        if "modified_by" in resp and resp["modified_by"] is not None:
            user = User.objects.filter(pk=resp["modified_by"]).first()
            if user is not None:
                resp["modified_by"] = UserBasicDetailSerializer(user).data
            else:
                resp["modified_by"] = {}

        return resp

class CompanySerializer(serializers.ModelSerializer):
    full_address = serializers.CharField(read_only=True)

    class Meta:
        model = Company
        fields = ("id", "name", "email", "phone", "full_address", "logo_url")

class CompanyDetailSerializer(WhoDidSerializerMixin, serializers.ModelSerializer):
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

class UserDetailSerializer(WhoDidSerializerMixin, EnumSupportSerializerMixin, serializers.ModelSerializer):
    company_details     = CompanySerializer(source="company", read_only=True)
    full_address        = serializers.CharField(read_only=True)

    class Meta:
        model = User
        exclude = ("password", "groups", "user_permissions", "date_joined", )
        extra_kwargs = {
            'company': {'write_only': True},
        }

