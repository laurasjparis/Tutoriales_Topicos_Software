"""
products/views.py
=================
VIEWS CON ORM DE DJANGO
─────────────────────────────────────────────────────────────────
MVC Role: CONTROLLER
  - Utilizamos Product.objects.all() en lugar de memoria estática.
  - Añadimos validación con get_object_or_404.
  - Demostramos el uso de ListView.
─────────────────────────────────────────────────────────────────
"""

from django.views.generic import TemplateView, View, ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


# ── 1A.  Product Index Original (TemplateView + ORM manual) ──────

class ProductIndexView(TemplateView):
    """
    Lista todos los productos utilizando Product.objects.all().
    """
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuestros Productos'
        context['header_title'] = 'Catálogo ORM'
        
        # OBTENER TODOS LOS REGISTROS DESDE SQL (SELECT * FROM products_product)
        context['products'] = Product.objects.all()
        return context


# ── 1B.  Product List View (Bonus: Usando ListView) ──────────────

class ProductListView(ListView):
    """
    Lista utilizando generic.ListView
    Django inyecta automáticamente 'object_list' o context_object_name.
    """
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products' # Igual que arriba

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Generic ListView'
        context['header_title'] = 'Catálogo ListView'
        return context


# ── 2.   Product Show (Detail View + 404/Redirección) ────────────

class ProductShowView(TemplateView):
    template_name = 'products/show.html'

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('id')

        # Buscar en BD o disparar except -> redireccionar
        try:
            # Busca 'id' exacto o falla
            product = get_object_or_404(Product, id=product_id)
        except Exception:
            # Feature: redirect to home if invalid
            return redirect('pages:home')

        return render(request, self.template_name, {
            'title': product.name,
            'header_title': 'Detalles',
            'product': product,
        })


# ── 3.   Product Create (ModelForm Save) ─────────────────────────

class ProductCreateView(View):
    """
    CREATE VIEW (ModelForm)
    A diferencia de form.Form, ModelForm.save() guarda en SQL de inmediato.
    """
    template_name = 'products/create.html'

    def get(self, request):
        return render(request, self.template_name, {
            'title': 'Crear Producto',
            'header_title': 'Nuevo Modelo',
            'form': ProductForm(),
        })

    def post(self, request):
        form = ProductForm(request.POST)

        if form.is_valid():
            # INSERTA EN DB: INSERT INTO products_product ... 
            product = form.save()
            return render(request, self.template_name, {
                'title': 'Crear Producto',
                'header_title': 'Nuevo Modelo',
                'form': ProductForm(),
                'success': True,
                'submitted': {
                    'name': product.name,
                    'price': product.price,
                },
            })

        return render(request, self.template_name, {
            'title': 'Crear Producto',
            'header_title': 'Nuevo Modelo',
            'form': form,
            'success': False,
        })
