from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from user.views import *
from customer.views import *

router = DefaultRouter()

router.register('nguoidung', NguoiDungViewSet)
router.register('customer', CustomerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((router.urls, 'nguoidung'), namespace='nguoidung')),
    path('', include((router.urls, 'customer'), namespace='customer')),
    
    path('check-user/', check_user),
]