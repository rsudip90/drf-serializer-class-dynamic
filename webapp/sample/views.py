from rest_framework import viewsets

from .mixins import GetSerializerClassMixin
from .models import User, Company, SystemUserRole
from .serializers import (
    CompanySerializer,
    CompanyDetailSerializer,
    UserSerializer,
    UserDetailSerializer,
)

class CompanyViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
    serializer_action_classes = {
        'list': CompanySerializer,
    }
    filterset_fields = ("country", "state", "city", )
    search_fields = ("name", "email", )
    ordering_fields = ("name", "country", )
    ordering = ("-created_at", )

# class UserViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserDetailSerializer
#     serializer_action_classes = {
#         'list': UserSerializer,
#     }
#     filterset_fields = ("country", "state", "city", "zipcode", "company", )
#     search_fields = ("first_name", "last_name", "email", )
#     ordering_fields = ("first_name", "last_name", "email", )
#     ordering = ("-created_at", )

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    serializer_detail_class = UserDetailSerializer
    filterset_fields = ("country", "state", "city", "zipcode", "company", )
    search_fields = ("first_name", "last_name", "email", )
    ordering_fields = ("first_name", "last_name", "email", )
    ordering = ("-created_at", )

    def get_serializer_class(self):
        """
        Special case to see the user full details.
        Unless user is request.user or SYS_ADMIN for user's company
        only show basic details of user.
        """

        lookup = self.lookup_url_kwarg or self.lookup_field
        if lookup and lookup in self.kwargs:

            # get detailed endpoint value from url e.g, "/users/2/" => 2
            user_pk = self.kwargs[lookup]
            lookup_user = User.objects.filter(pk=user_pk).first()

            # if current user is looking at the details
            if self.request.user == lookup_user:
                return self.serializer_detail_class

            # if current user is sys admin of the requested user's company
            if (self.request.user.system_role == SystemUserRole.SYS_ADMIN and
                self.request.user.company == lookup_user.company):
                return self.serializer_detail_class

            return super().get_serializer_class()
        else:
            return super().get_serializer_class()

