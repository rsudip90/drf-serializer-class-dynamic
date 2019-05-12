from rest_framework import routers
from sample import views

APIRouter = routers.DefaultRouter()
APIRouter.register(r'users', views.UserViewSet, basename="users")
APIRouter.register(r'companies', views.CompanyViewSet, basename="companies")

