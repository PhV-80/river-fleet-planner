from rest_framework.routers import DefaultRouter
from .views import ShipViewSet, VoyageViewSet

router = DefaultRouter()
router.register(r'ships', ShipViewSet)
router.register(r'voyages', VoyageViewSet)

urlpatterns = router.urls