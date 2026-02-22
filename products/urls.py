"""
products/urls.py
================
URL PATTERNS FOR THE PRODUCTS APP
─────────────────────────────────────────────────────────────────
MVC Role: ROUTER
  Routes:
    /products/              → ProductIndexView (list)
    /products/create/       → ProductCreateView (form)
    /products/<id>/         → ProductShowView (detail)

  Note: 'create/' is declared BEFORE '<id>/' so Django never
  tries to cast the string "create" as an integer id.
─────────────────────────────────────────────────────────────────
"""

from django.urls import path
from .views import ProductIndexView, ProductShowView, ProductCreateView, ProductListView

app_name = 'products'  # URL namespace

urlpatterns = [
    # /products/
    path('', ProductIndexView.as_view(), name='index'),

    # /products/create/  ← must come BEFORE <id>
    path('create/', ProductCreateView.as_view(), name='create'),

    # Bonus: /products/list/  ← usando el ListView genérico
    path('list/', ProductListView.as_view(), name='list'),

    # /products/<id>/  e.g. /products/3/
    path('<int:id>/', ProductShowView.as_view(), name='show'),
]
