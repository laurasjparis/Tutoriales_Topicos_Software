"""
products/views.py
=================
VIEWS FOR THE PRODUCTS MODULE
─────────────────────────────────────────────────────────────────
MVC Role: CONTROLLER
  - Views receive HTTP requests, consult the Model, build context,
    and delegate rendering to the Template layer.

Views defined here:
  ProductIndexView  — Lists all products          GET /products/
  ProductShowView   — Shows one product detail    GET /products/<id>/
  ProductCreateView — Shows and handles the form  GET|POST /products/create/
─────────────────────────────────────────────────────────────────
"""

from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect

from .models import get_all_products, get_product_by_id
from .forms import ProductForm


# ── 1.  Product Index ────────────────────────────────────────────

class ProductIndexView(TemplateView):
    """
    LIST VIEW — shows all products.
    Uses TemplateView because it's a simple read-only page.

    URL:      /products/
    Template: templates/products/index.html
    """
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Our Products'
        context['header_title'] = 'Product Catalogue'
        # ── Call Model layer to retrieve data ──────────────────
        context['products'] = get_all_products()
        return context


# ── 2.  Product Show (Detail) ────────────────────────────────────

class ProductShowView(TemplateView):
    """
    DETAIL VIEW — shows a single product identified by <id>.

    URL:      /products/<id>/
    Template: templates/products/show.html
    Redirect: If the id doesn't match any product → redirect to home.
    """
    template_name = 'products/show.html'

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('id')

        # ── Query Model layer ──────────────────────────────────
        product = get_product_by_id(product_id)

        if product is None:
            # Feature 8: invalid id → redirect to home
            return redirect('pages:home')

        return render(request, self.template_name, {
            'title': product.name,
            'header_title': 'Product Detail',
            'product': product,
        })


# ── 3.  Product Create (Form) ────────────────────────────────────

class ProductCreateView(View):
    """
    CREATE VIEW — renders the form (GET) and processes it (POST).

    Uses the base View class to show explicit GET / POST handling,
    which mirrors the MVC / HTTP verb pattern taught in class.

    URL:      /products/create/
    Template: templates/products/create.html
    """
    template_name = 'products/create.html'

    # ── GET: Render empty form ─────────────────────────────────
    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {
            'title': 'Add Product',
            'header_title': 'New Product',
            'form': form,
        })

    # ── POST: Validate and process form data ───────────────────
    def post(self, request):
        form = ProductForm(request.POST)

        if form.is_valid():
            # In a real project you'd save to the database here.
            # For the tutorial we simply read the cleaned values.
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            category = form.cleaned_data['category']
            description = form.cleaned_data.get('description', '')

            # Pass success message and submitted data to template
            return render(request, self.template_name, {
                'title': 'Add Product',
                'header_title': 'New Product',
                'form': ProductForm(),        # fresh empty form
                'success': True,
                'submitted': {
                    'name': name,
                    'price': price,
                    'category': category,
                    'description': description,
                },
            })

        # Form is INVALID → re-render with error messages
        return render(request, self.template_name, {
            'title': 'Add Product',
            'header_title': 'New Product',
            'form': form,                     # form carries errors
            'success': False,
        })
