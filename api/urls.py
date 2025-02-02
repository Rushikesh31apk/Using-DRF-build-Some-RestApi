from django.contrib import admin
from django.urls import path, include  # Import `include`
from rest_framework import routers
from api.views import CompanyViewSet, EmployeeViewSet

# Create router and register the viewset
router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees',EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Use `router.urls` here
]
