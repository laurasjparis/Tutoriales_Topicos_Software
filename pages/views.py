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
