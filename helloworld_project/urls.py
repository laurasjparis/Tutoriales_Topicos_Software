"""
helloworld_project/urls.py
==========================
ROOT URL CONFIGURATION
─────────────────────────────────────────────────────────────────
MVC Role: CONTROLLER entry-point
  - Django's root urls.py acts as the front-controller.
  - It delegates URL namespaces to each app via include().

NOTA SOBRE RUTAS DE IMAGEN:
  Las rutas /image/ e /imagenotdi/ se definen AQUÍ (sin namespace)
  para que redirect('image_index') y {% url 'image_save' %} funcionen
  directamente desde templates y views sin prefijo de namespace.
─────────────────────────────────────────────────────────────────
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import ImageViewFactory, ImageViewNoDI
from pages.utils import ImageLocalStorage

urlpatterns = [
    # Django admin (keep for reference)
    path('admin/', admin.site.urls),

    # ── Pages app  →  handles:  /  /about/  /cart/  (con namespace 'pages')
    path('', include('pages.urls')),

    # ── Products app  →  handles:  /products/  and  /products/<id>/
    path('products/', include('products.urls')),

    # ── Image Storage: VERSION CON DIP/DI ─────────────────────────────────────
    # Sin namespace para que 'image_index' e 'image_save' funcionen sin prefijo.
    # ImageViewFactory recibe ImageLocalStorage() INYECTADO desde aquí.
    # Para cambiar a S3: ImageViewFactory(ImageS3Storage()) ← sólo esta línea.
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),

    # ── Image Storage: VERSION SIN DIP (acoplada) ─────────────────────────────
    # Endpoint distinto para que ambas versiones convivan sin colisión de rutas.
    path('imagenotdi/', ImageViewNoDI.as_view(), name='imagenotdi_index'),
    path('imagenotdi/save', ImageViewNoDI.as_view(), name='imagenotdi_save'),
]

# ── Media files en desarrollo ─────────────────────────────────────────────────
# En producción, nginx/apache sirven /media/. En DEBUG lo hace Django.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

