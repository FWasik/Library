"""django_library_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as views_auth
from library import views as views_lib
from users import views as views_users
from library.views import (
    OrderListView, 
    OrderCreateView, 
    OrderDeleteView, 
    OrderDetailView,
    OrderUpdateView
)

from users.views import UserDeleteView
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_lib.home, name='lib-home'),
    path('about/', views_lib.about, name='lib-about'),
    path('gallery/', views_lib.gallery, name='lib-gallery'),
    path('register/', views_users.register, name='users-register'),
    path('login/', views_auth.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', views_auth.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),

    path('profile/', OrderListView.as_view(), name='profile-orders-list'),
    path('profile/orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    path('profile/orders/order_create/', OrderCreateView.as_view(), name='order-create'),
    path('profile/orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('profile/orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('profile/update/', views_users.profile, name='profile-update'),
    path('profile/<int:pk>/delete/', UserDeleteView.as_view(), name='profile-delete'),

    path('profile/password-reset/', views_auth.PasswordResetView.as_view(template_name='users/password_reset.html'), name='users-password-reset'),
    path('profile/password-reset/done/', views_auth.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('profile/password-reset-confirm/<uidb64>/<token>/', views_auth.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('profile/password-reset-complete/', views_auth.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
