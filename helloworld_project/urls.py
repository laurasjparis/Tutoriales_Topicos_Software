"""
helloworld_project/urls.py
==========================
ROOT URL CONFIGURATION
─────────────────────────────────────────────────────────────────
MVC Role: CONTROLLER entry-point
  - Django's root urls.py acts as the front-controller.
  - It delegates URL namespaces to each app via include().
─────────────────────────────────────────────────────────────────
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin (keep for reference)
    path('admin/', admin.site.urls),

    # ── Pages app  →  handles:  /  and  /about/
    path('', include('pages.urls')),

    # ── Products app  →  handles:  /products/  and  /products/<id>/
    path('products/', include('products.urls')),
]
