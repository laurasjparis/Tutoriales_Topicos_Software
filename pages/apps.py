"""
pages/apps.py
=============
SERVICE PROVIDER (AppConfig)
─────────────────────────────────────────────────────────────────
DIP Role: CONFIGURACIÓN DEL PROVIDER
  - El método ready() se ejecuta UNA SOLA VEZ cuando Django arranca.
  - import_string() carga dinámicamente la clase indicada en
    settings.IMAGE_STORAGE_CLASS.
  - Para cambiar de LOCAL a S3 basta con editar settings.py:
      IMAGE_STORAGE_CLASS = 'pages.utils.ImageS3Storage'
    Las Views nunca cambian.
─────────────────────────────────────────────────────────────────
"""

from django.apps import AppConfig
from django.utils.module_loading import import_string
from django.conf import settings


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'

    def ready(self):
        # Carga la clase concreta de almacenamiento definida en settings.
        # Ejemplo: 'pages.utils.ImageLocalStorage'
        # Para cambiar de backend, solo cambia el string en settings.py.
        ImageStorageClass = import_string(settings.IMAGE_STORAGE_CLASS)
        # ImageStorageClass está disponible para usarse como provider.
        # Las views lo reciben vía inyección en ImageViewFactory.
