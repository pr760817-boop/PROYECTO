from django.contrib import admin
from django.urls import path, include
from app_usuario import views

urlpatterns = [
    path('admin/', admin.site.rules if hasattr(admin.site, 'rules') else admin.site.urls),
    path('', views.inicio, name='inicio'),  # Renderiza directamente inicio en http://127.0.0.1:8000/
    path('usuarios/', include('app_empleate.urls')),
]