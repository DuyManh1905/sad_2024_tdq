from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('add-book-cart/', views.add_book_to_cart, name='add-book-cart'),
    path('add-clothes-cart/', views.add_clothes_to_cart, name='add-clothes-cart'),
    path('add-mobile-cart/', views.add_mobile_to_cart, name='add-mobile-cart'),
    path('cart-detail/', views.get_cart, name='cart'),
    path('search-page/', views.get_search_page, name='search-page'),
    path('search/', views.search, name='search'),
    path('search-voice/', views.search_voice, name='search-voice'),
    path('order-form/', views.order_form, name='order-form'),
    path('create-order', views.add_order, name='add-order'),
    path('list-order/', views.get_list_order, name='list-order'),
    path('detail-order/<int:order_id>/', views.detail_order, name='detail-order'),
    path('cancel-order/', views.cancel_order, name='cancel-order'),
]
