from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shipment import views

router = DefaultRouter()
router.register('shipment', views.ShipmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((router.urls, 'shipment'), namespace='shipment')),
    path('update-shipment/', views.update_shipment),
    path('shipment-status/', views.shipment_status),
]
