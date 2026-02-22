"""
products/forms.py
=================
MODEL FORM — Conversión Automática Modelo → Formulario
─────────────────────────────────────────────────────────────────
MVC Role: MODEL / CONTROLLER
  - En lugar de forms.Form, heredamos de forms.ModelForm.
  - Genera automáticamente los campos HTML basados en la base de datos.
  - Implementa clean_<field> para validación extra.
─────────────────────────────────────────────────────────────────
"""

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """
    Formulario basado en el Modelo Product.
    Mapea campos del Modelo directamente al HTML.
    """
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
        
        # Personalizamos los widgets para aplicar CSS Bootstrap 5
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Teclado Mecánico',
                'autofocus': True,
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Breve descripción de su producto...',
                'rows': 3,
            }),
        }

    def clean_price(self):
        """
        Validación personalizada.
        Verificamos que el precio sea mayor a 0 según requerimientos.
        """
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError('El precio debe ser un número entero mayor a 0.')
        return price
