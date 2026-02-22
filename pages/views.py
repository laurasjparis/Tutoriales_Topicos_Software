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
        context['header_title'] = 'Your Favourite Online Store'
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
