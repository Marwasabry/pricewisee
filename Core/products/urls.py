from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, ProductViewSet
from .views import process_image

router = DefaultRouter()
#router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('process_image/',process_image, name='process_image'),

]
