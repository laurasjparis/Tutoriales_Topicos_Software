"""
products/models.py
==================
MODELOS DE BASE DE DATOS — Django ORM
─────────────────────────────────────────────────────────────────
MVC Role: MODEL
  - Los modelos definen la estructura de las tablas en la base de datos.
  - Django ORM traduce clases Python → tablas SQL automáticamente.
  - Cada instancia de un modelo = una fila en la tabla.

Modelos definidos aquí:
  Product  — tabla de productos
  Comment  — tabla de comentarios (relación FK con Product)
─────────────────────────────────────────────────────────────────

COMANDOS CLAVE:
  python manage.py makemigrations
    → Lee los modelos y genera archivos de migración en products/migrations/
    → Es como un "borrador" de los cambios en el esquema SQL.

  python manage.py migrate
    → Ejecuta los archivos de migración y aplica los cambios a la BD.
    → Crea o modifica las tablas físicas en db.sqlite3.
─────────────────────────────────────────────────────────────────
"""

from django.db import models


# ══════════════════════════════════════════════════════════════
# MODELO: Product
# Tabla SQL generada: products_product
# ══════════════════════════════════════════════════════════════

class Product(models.Model):
    """
    Representa un producto en la tienda.

    Campos:
        name       — Nombre del producto (VARCHAR 200)
        price      — Precio en USD (INTEGER)
        created_at — Fecha de creación (se rellena automáticamente)
        updated_at — Fecha de última actualización (se actualiza sola)
    """

    name = models.CharField(
        max_length=200,
        verbose_name='Nombre del producto',
    )

    price = models.IntegerField(
        verbose_name='Precio (USD)',
    )

    description = models.TextField(
        verbose_name='Descripción',
        blank=True,
        null=True,
    )

    # auto_now_add=True → el campo se asigna UNA SOLA VEZ al crear el objeto
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creado el',
    )

    # auto_now=True → el campo se actualiza EN CADA save()
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Actualizado el',
    )

    class Meta:
        # Orden por defecto: más reciente primero
        ordering = ['-created_at']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """
        Representación legible del objeto.
        Aparece en el Admin y en el shell de Django.
        """
        return f'{self.name} (${self.price})'


# ══════════════════════════════════════════════════════════════
# MODELO: Comment
# Tabla SQL generada: products_comment
# ══════════════════════════════════════════════════════════════

class Comment(models.Model):
    """
    Representa un comentario asociado a un producto.

    RELACIÓN: Un Product puede tener MUCHOS Comment (One-to-Many).
    La clave foránea (ForeignKey) se almacena en la tabla Comment
    como la columna product_id.

    on_delete=models.CASCADE significa:
      Si el Product es eliminado, todos sus comentarios
      también se eliminan automáticamente (borrado en cascada).
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments',     # permite product.comments.all()
        verbose_name='Producto',
    )

    description = models.TextField(
        verbose_name='Comentario',
    )

    # Fecha de creación automática
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Publicado el',
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f'Comentario en "{self.product.name}"'
