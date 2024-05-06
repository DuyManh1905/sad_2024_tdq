from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cart import views as cart_views
from cart_book import views as cart_book_views
from cart_clothes import views as cart_clothes_views
from cart_mobile import views as cart_mobile_views

router = DefaultRouter()
router.register('cart', cart_views.CartViewSet),
router.register('cart-book', cart_book_views.CartBookViewSet),
router.register('cart-clothes', cart_clothes_views.CartClothesViewSet),
router.register('cart-mobile', cart_mobile_views.CartMobileViewSet),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((router.urls, 'cart'), namespace='cart')),
    path('', include((router.urls, 'cart-book'), namespace='cart-book')),
    path('', include((router.urls, 'cart-clothes'), namespace='cart-clothes')),
    path('', include((router.urls, 'cart-mobile'), namespace='cart-mobile')),
    
    path('add-book-cart/', cart_book_views.add_book_cart),
    path('add-clothes-cart/', cart_clothes_views.add_clothes_cart),
    path('add-mobile-cart/', cart_mobile_views.add_mobile_cart),
    path('cart_id/', cart_views.get_id_cart),
    path('cart-detail/', cart_views.get_cart),
    path('delete/', cart_views.delete_cart),
]
