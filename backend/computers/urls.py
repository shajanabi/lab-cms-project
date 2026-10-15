from rest_framework.routers import DefaultRouter

from .views import ComputerViewSet


router = DefaultRouter()
router.register('', ComputerViewSet, basename='computer')

urlpatterns = router.urls