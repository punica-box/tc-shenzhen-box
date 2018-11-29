"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

app_name = 'api'

from rest_framework.routers import DefaultRouter

from ontofraud.views import WalletViewSet, WalletView, MainPageView

router = DefaultRouter()

router.register('api/v1/wallets', WalletViewSet, base_name='wallets')

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('wallet/<slug>/', WalletView.as_view(), name='wallet'),
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
