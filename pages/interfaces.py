"""
pages/interfaces.py
===================
INTERFACE: ImageStorage (Dependency Inversion Principle)
─────────────────────────────────────────────────────────────────
DIP Role: ABSTRACTION
  - Define el contrato al que deben adherirse TODAS las
    implementaciones de almacenamiento de imágenes.
  - Las Views (alto nivel) dependen de esta abstracción,
    NO de la implementación concreta (bajo nivel).
─────────────────────────────────────────────────────────────────
"""

from abc import ABC, abstractmethod
from django.http import HttpRequest


class ImageStorage(ABC):
    """
    Interfaz abstracta para almacenamiento de imágenes.

    Cualquier clase que la herede DEBE implementar el método `store`.
    Esto garantiza que las Views nunca dependan de una implementación
    concreta (e.g. local, S3, GCS), sino sólo de este contrato.
    """

    @abstractmethod  # any class that inherits from this one must implement this method
    def store(self, request: HttpRequest):
        pass
