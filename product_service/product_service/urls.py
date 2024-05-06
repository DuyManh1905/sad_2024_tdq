from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from book import views as book_views
from mobile import views as mobile_views
from clothes import views as clothes_views

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

router.register('book', book_views.BookViewSet)
router.register('category-book', book_views.CategoryBookViewSet)
router.register('author', book_views.AuthorViewSet)
router.register('publisher', book_views.PublisherViewSet)

router.register('clothes', clothes_views.ClothesViewSet)
router.register('category-clothes', clothes_views.CategoryClothesViewSet)

router.register('mobile', mobile_views.MobileViewSet)
router.register('category-mobile', mobile_views.CategoryMobileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((router.urls, 'book'), namespace='book')),
    path('', include((router.urls, 'category-book'), namespace='category-book')),
    path('', include((router.urls, 'author'), namespace='author')),
    path('', include((router.urls, 'publisher'), namespace='publisher')),
    
    path('', include((router.urls, 'clothes'), namespace='clothes')),
    path('', include((router.urls, 'category-clothes'), namespace='category-clothes')),
    
    path('', include((router.urls, 'mobile'), namespace='mobile')),
    path('', include((router.urls, 'category-mobile'), namespace='category-mobile')),
    
    path('books/', book_views.get_list_book, name='books'),
    path('detail/book/', book_views.get_detail_book),
    path('clothes-all/', clothes_views.get_list_clothes, name='clothes-all'),
    path('detail/clothes/', clothes_views.get_detail_clothes),
    path('mobiles/', mobile_views.get_list_mobile, name='mobiles'),
    path('detail/mobile/', mobile_views.get_detail_mobile),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
