from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order import views

router = DefaultRouter()
router.register('order', views.OrderViewSet),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((router.urls, 'order'), namespace='order')),
    
    path('add-order/', views.add_order),
    path('list-order/', views.get_list_order),
    path('detail-order/', views.detail_order),
]
