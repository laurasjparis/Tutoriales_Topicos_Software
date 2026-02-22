"""
pages/management/commands/seed_products.py
==========================================
COMANDO DE GESTIÓN (SEEDER)
─────────────────────────────────────────
Comando personalizado para poblar la BBDD.
Se ejecuta con: python manage.py seed_products
"""

from django.core.management.base import BaseCommand
from products.factories import ProductFactory, CommentFactory

class Command(BaseCommand):
    help = 'Crea productos y comentarios de prueba automáticamente'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Eliminando datos anteriores...'))
        # Limpiamos antes de generar (opcional, pero útil)
        from products.models import Product
        Product.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Generando productos con Factory Boy / Faker...'))
        
        # create_batch(8) crea 8 productos y los guarda en base de datos
        products = ProductFactory.create_batch(8)

        # Generar un par de comentarios para cada producto
        for product in products:
            CommentFactory.create_batch(2, product=product)

        self.stdout.write(self.style.SUCCESS('¡Éxito! Se crearon 8 productos y sus comentarios.'))
