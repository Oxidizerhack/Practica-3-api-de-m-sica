"""
URL configuration for apimusica project.

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
from django.urls import path, include
from musica import views as musica_views
from rest_framework import DefaultRouter    

router = DefaultRouter()
router.register(r'ritmos', musica_views.views.RitmoViewSet)
router.register(r'instrumentos', musica_views.InstrumentoViewSet)
router.register(r'departamentos', musica_views.DepartamentoViewSet)
router.register(r'agrupaciones', musica_views.AgrupacionViewSet)
router.register(r'canciones', musica_views.CancionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # ← Aquí va la API
]

