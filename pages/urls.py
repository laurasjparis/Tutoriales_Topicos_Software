"""
pages/urls.py
=============
URL PATTERNS FOR THE PAGES APP
─────────────────────────────────────────────────────────────────
MVC Role: ROUTER (part of Controller layer)
  - Maps URL patterns to la corresponding View class.
  - app_name = 'pages' habilita el namespace  {% url 'pages:home' %}
    SÓLO para las rutas listadas aquí.

NOTA IMPORTANTE SOBRE NAMESPACING:
  Las rutas de imagen (image/, imagenotdi/) NO están aquí — están en
  helloworld_project/urls.py directamente (sin namespace), para que
  redirect('image_index') y {% url 'image_save' %} funcionen sin prefijo.
─────────────────────────────────────────────────────────────────
"""

from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    CartView,
    CartRemoveAllView,
)

app_name = 'pages'  # URL namespace

urlpatterns = [
    # ── Pages ─────────────────────────────────────────────────────────────────
    # Route: /  →  HomePageView
    path('', HomePageView.as_view(), name='home'),

    # Route: /about/  →  AboutPageView
    path('about/', AboutPageView.as_view(), name='about'),

    # ── Cart ──────────────────────────────────────────────────────────────────
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
]
