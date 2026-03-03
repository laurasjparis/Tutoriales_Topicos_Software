"""
pages/views.py
==============
VIEWS FOR THE PAGES APP
─────────────────────────────────────────────────────────────────
MVC Role: VIEW (in Django this is the Controller logic layer)
  - TemplateView is a Django class-based view that renders a template.
  - get_context_data() feeds dynamic data (the "Model" data) into
    the template.
─────────────────────────────────────────────────────────────────
"""

from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render, redirect
from products.models import Product
from .utils import ImageLocalStorage


class HomePageView(TemplateView):
    """
    Renders the Home page.
    Template: templates/pages/home.html
    URL:      /
    """
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        # Call parent method to get the base context dictionary
        context = super().get_context_data(**kwargs)
        # Inject custom data into the template context
        context['title'] = 'Welcome to the Online Store'
        context['header_title'] = 'A django EAFIT app'
        context['tagline'] = 'Quality products delivered to your door.'
        return context


class AboutPageView(TemplateView):
    """
    Renders the About page.
    Template: templates/pages/about.html
    URL:      /about/
    """
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['header_title'] = 'About Our Store'
        context['subtitle'] = 'Our Mission'
        context['description'] = (
            'We are a passionate team dedicated to bringing you the best '
            'products at unbeatable prices. Founded in 2020, our store has '
            'grown from a small idea into a thriving online marketplace.'
        )
        context['author'] = 'Laura Jiménez'
        return context


class CartView(View):
    template_name = 'cart/index.html'

    def get(self, request):
        # Database products
        db_products = Product.objects.all()
        products = {str(p.id): p for p in db_products}

        # Get cart products from session
        cart_products = {}
        cart_product_data = request.session.get('cart_product_data', {})

        for key, product in products.items():
            if str(key) in cart_product_data.keys():
                cart_products[key] = product

        # Prepare data for the view
        view_data = {
            'title': 'Cart - Online Store',
            'subtitle': 'Shopping Cart',
            'products': products,
            'cart_products': cart_products
        }

        return render(request, self.template_name, view_data)

    def post(self, request, product_id):
        # Get cart products from session and add the new product
        cart_product_data = request.session.get('cart_product_data', {})
        cart_product_data[product_id] = product_id
        request.session['cart_product_data'] = cart_product_data

        return redirect('pages:cart_index')


class CartRemoveAllView(View):
    def post(self, request):
        # Remove all products from cart in session
        if 'cart_product_data' in request.session:
            del request.session['cart_product_data']

        return redirect('pages:cart_index')


# ══════════════════════════════════════════════════════════════════════════════
# VERSIÓN CON DEPENDENCY INVERSION + DEPENDENCY INJECTION
# ══════════════════════════════════════════════════════════════════════════════

def ImageViewFactory(image_storage):
    """
    View Factory — Patrón DIP + DI
    ─────────────────────────────────────────────────────────────────
    DÓNDE ESTÁ LA INVERSIÓN (DIP):
      - La función recibe un objeto que IMPLEMENTA la interfaz
        ImageStorage (abstracción), sin importar si es local, S3, GCS.
      - ImageView (alto nivel) depende de la ABSTRACCIÓN, no de
        ImageLocalStorage (bajo nivel). La dependencia está invertida.

    DÓNDE ESTÁ LA INYECCIÓN (DI):
      - En pages/urls.py se llama:
            ImageViewFactory(ImageLocalStorage())
        El objeto concreto se INYECTA desde afuera (desde el router),
        no se construye dentro de la view.
    ─────────────────────────────────────────────────────────────────
    """
    class ImageView(View):
        template_name = 'images/index.html'

        def get(self, request):
            # Recupera la URL de la imagen guardada en sesión
            image_url = request.session.get('image_url', '')
            return render(request, self.template_name, {'image_url': image_url})

        def post(self, request):
            # Delega el almacenamiento al objeto inyectado (image_storage)
            # La View no sabe ni le importa si es local, S3 o GCS.
            image_url = image_storage.store(request)
            request.session['image_url'] = image_url
            return redirect('image_index')

    return ImageView


# ══════════════════════════════════════════════════════════════════════════════
# VERSIÓN SIN DEPENDENCY INVERSION (acoplada)
# ══════════════════════════════════════════════════════════════════════════════

class ImageViewNoDI(View):
    """
    View SIN Dependency Inversion — Versión acoplada
    ─────────────────────────────────────────────────────────────────
    PROBLEMA:
      - La view instancia ImageLocalStorage() directamente en post().
      - Si mañana se quiere usar S3, hay que MODIFICAR esta clase.
      - Viola el principio de abierto/cerrado (OCP) y DIP.
      - Es difícil de testear (no se puede inyectar un mock).
    ─────────────────────────────────────────────────────────────────
    """
    template_name = 'imagesnotdi/index.html'

    def get(self, request):
        image_url = request.session.get('image_url', '')
        return render(request, self.template_name, {'image_url': image_url})

    def post(self, request):
        # ACOPLAMIENTO: la view decide y construye su propia dependencia.
        # Para cambiar de backend hay que editar ESTA clase.
        image_storage = ImageLocalStorage()
        image_url = image_storage.store(request)
        request.session['image_url'] = image_url
        return redirect('imagenotdi_index')
