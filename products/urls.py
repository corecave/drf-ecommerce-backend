from django.urls import path
from rest_framework.routers import SimpleRouter

from products.views import ProductViewSet

router = SimpleRouter()

router.register('', ProductViewSet)

urlpatterns = [
              ] + router.urls
