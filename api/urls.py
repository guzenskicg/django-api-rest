from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, PersonViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
