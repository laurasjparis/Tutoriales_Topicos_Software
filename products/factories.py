"""
products/factories.py
=====================
FACTORIES — Generación de datos de prueba
─────────────────────────────────────────
Utilizamos factory-boy y Faker para poblar (seed) la base de datos
con datos ficticios pero realistas sin tener que crearlos a mano.
"""

import factory
from products.models import Product, Comment

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    # Faker: Genera nombres de productos aleatorios y precios
    name = factory.Faker('catch_phrase')
    price = factory.Faker('random_int', min=100, max=3000)

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    product = factory.SubFactory(ProductFactory)
    description = factory.Faker('text', max_nb_chars=150)
