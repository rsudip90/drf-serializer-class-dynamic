from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from .router import APIRouter

schema_view = get_swagger_view(title='Sample API')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", schema_view),
    path("api/v1/", include(APIRouter.urls)),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework'))
]

