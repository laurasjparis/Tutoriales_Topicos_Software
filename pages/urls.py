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
from .views import HomePageView, AboutPageView

app_name = 'pages'  # URL namespace

urlpatterns = [
    # Route: /  →  HomePageView
    path('', HomePageView.as_view(), name='home'),

    # Route: /about/  →  AboutPageView
    path('about/', AboutPageView.as_view(), name='about'),
]
