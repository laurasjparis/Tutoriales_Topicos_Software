"""
pages/utils.py
==============
IMPLEMENTACIÓN CONCRETA: ImageLocalStorage
─────────────────────────────────────────────────────────────────
DIP Role: MÓDULO DE BAJO NIVEL
  - Implementa el contrato definido en ImageStorage.
  - Usa el sistema de archivos local como backend.
  - Si en el futuro se desea usar S3, se crea ImageS3Storage
    que también herede de ImageStorage, y sólo se cambia
    IMAGE_STORAGE_CLASS en settings.py. Las Views no cambian.
─────────────────────────────────────────────────────────────────
"""

from django.core.files.storage import default_storage
from django.http import HttpRequest
from .interfaces import ImageStorage


class ImageLocalStorage(ImageStorage):
    """
    Implementación concreta que guarda imágenes en el filesystem local.

    Usa default_storage de Django, que respeta MEDIA_ROOT / MEDIA_URL
    definidos en settings.py.
    """

    def store(self, request: HttpRequest):
        """
        Lee el archivo 'profile_image' del request, lo guarda en
        'media/uploaded_images/' y retorna la URL pública.
        Retorna None si no se subió ningún archivo.
        """
        profile_image = request.FILES.get('profile_image', None)
        if profile_image:
            # Guardar el archivo en media/uploaded_images/<nombre>
            file_name = default_storage.save(
                'uploaded_images/' + profile_image.name,
                profile_image
            )
            return default_storage.url(file_name)
        return None
