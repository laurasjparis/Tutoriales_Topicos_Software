"""
products/models.py
==================
MODEL LAYER — Data & Business Logic
─────────────────────────────────────────────────────────────────
MVC Role: MODEL
  - In this tutorial we use a plain Python class (no database ORM)
    to keep things simple and focus on the MVC pattern.
  - In a real project you'd extend django.db.models.Model instead.
─────────────────────────────────────────────────────────────────
"""


class Product:
    """
    Represents a single product in our Online Store.

    Attributes:
        id          (int):  Unique identifier.
        name        (str):  Product name shown to the user.
        description (str):  Short description of the product.
        price       (float): Price in USD.
        category    (str):  Product category label.
        emoji       (str):  Decorative emoji for the card.
    """

    def __init__(self, id, name, description, price, category, emoji='🛍️'):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.emoji = emoji

    def __repr__(self):
        return f'<Product id={self.id} name="{self.name}">'


# ── In-memory product catalogue ────────────────────────────────
# Think of this as our "database" for this tutorial.
PRODUCTS = [
    Product(
        id=1,
        name='MacBook Pro 16"',
        description=(
            'Apple M3 Pro chip, 18 GB unified memory, 512 GB SSD. '
            'Perfect for developers and creative professionals.'
        ),
        price=2499.99,
        category='Electronics',
        emoji='💻',
    ),
    Product(
        id=2,
        name='Sony WH-1000XM5 Headphones',
        description=(
            'Industry-leading noise-cancelling headphones with 30-hour '
            'battery life and crystal-clear call quality.'
        ),
        price=349.99,
        category='Electronics',
        emoji='🎧',
    ),
    Product(
        id=3,
        name='Django for Professionals',
        description=(
            'Build production-ready Django web applications. Covers Docker, '
            'PostgreSQL, payment processing, and much more.'
        ),
        price=39.99,
        category='Books',
        emoji='📚',
    ),
    Product(
        id=4,
        name='Ergonomic Office Chair',
        description=(
            'Lumbar support, adjustable armrests, breathable mesh. '
            'Stay comfortable during those long coding sessions.'
        ),
        price=599.99,
        category='Furniture',
        emoji='🪑',
    ),
    Product(
        id=5,
        name='USB-C Hub 10-in-1',
        description=(
            '4K HDMI, 100 W PD, SD/MicroSD, 3× USB-A, Ethernet, '
            '3.5 mm audio. The only hub you will ever need.'
        ),
        price=79.99,
        category='Accessories',
        emoji='🔌',
    ),
    Product(
        id=6,
        name='Mechanical Keyboard',
        description=(
            'Compact TKL layout, Cherry MX Blue switches, RGB backlight. '
            'Satisfying tactile feedback for every keystroke.'
        ),
        price=129.99,
        category='Accessories',
        emoji='⌨️',
    ),
]


def get_all_products():
    """Return the full list of products."""
    return PRODUCTS


def get_product_by_id(product_id):
    """
    Find and return a single Product by its id.
    Returns None if no product with that id exists.
    """
    for product in PRODUCTS:
        if product.id == int(product_id):
            return product
    return None
