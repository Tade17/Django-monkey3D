"""
URL configuration for my_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views
from users import views as user_views
urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),
    # Include the URLs for each app
    
    path('users/', include('users.urls')),
    path('products/', include('products.urls'),name='home'),
    path('orders/', include('orders.urls')),
    path('marketing/', include('marketing.urls')),
    
    
    path('',core_views.home, name='home'),
    path('signup/',user_views.signup,name='signup'),
    
    # Esta línea maneja login, logout, reseteo de contraseña, etc.
    path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)