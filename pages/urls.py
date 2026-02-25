"""
pages/urls.py
=============
URL PATTERNS FOR THE PAGES APP
─────────────────────────────────────────────────────────────────
MVC Role: ROUTER (part of Controller layer)
  - Maps URL patterns to the corresponding View class.
  - app_name enables {% url 'pages:home' %} namespacing in templates.
─────────────────────────────────────────────────────────────────
"""

from django.urls import path
from .views import HomePageView, AboutPageView, CartView, CartRemoveAllView

app_name = 'pages'  # URL namespace

urlpatterns = [
    # Route: /  →  HomePageView
    path('', HomePageView.as_view(), name='home'),

    # Route: /about/  →  AboutPageView
    path('about/', AboutPageView.as_view(), name='about'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
]
