from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api_views import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]