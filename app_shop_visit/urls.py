from django.urls import path, include
from rest_framework import routers
from .api import StoreViewSet, VisitView

router = routers.DefaultRouter()
router.register(r'', StoreViewSet, 'app_shop_visit')

urlpatterns = [
    path('stores/', include(router.urls)),
    path('visit/', VisitView.as_view())
]
