from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .viewsets import PinDocumentView

router = DefaultRouter()
pin = router.register('pin',
                        PinDocumentView,
                        basename='pindocument')

urlpatterns = [
    url(r'^', include(router.urls)),
]