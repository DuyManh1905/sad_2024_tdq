from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    
    path('', views.get_home, name='home'),
    path('login-form/', views.login_form, name='login-form'),
    path('check-user/', views.check_login, name='check-login'),
    path('logout/', views.logout, name='logout'),
    path('book/<int:book_id>/', views.detail_book, name='detail-book'),
    path('clothes/<int:clothes_id>/', views.detail_clothes, name='detail-clothes'),
    path('mobile/<int:mobile_id>/', views.detail_mobile, name='detail-mobile'),
]