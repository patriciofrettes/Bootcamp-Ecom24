from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),                     # Rutas de la app accounts
    path('transactions/', include('transactions.urls')),  # Rutas de la app transactions
    path('administration/', include('administration.urls')),  # Rutas de la app administration
]

# Servir archivos estáticos y multimedia solo en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



