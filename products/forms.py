"""
products/forms.py
=================
DJANGO FORM — ProductForm
─────────────────────────────────────────────────────────────────
MVC Role: Part of MODEL / CONTROLLER
  - Forms in Django handle:
      1. Rendering HTML input fields
      2. Receiving POST data
      3. Validating user input
      4. Providing cleaned data to the View
─────────────────────────────────────────────────────────────────
"""

from django import forms


class ProductForm(forms.Form):
    """
    A form for creating a new product.

    Fields:
        name  — Product name (required, max 100 chars).
        price — Price in USD (required, must be positive).
    """

    name = forms.CharField(
        label='Product Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. Wireless Mouse',
            'autofocus': True,
        }),
        error_messages={
            'required': 'Please enter a product name.',
            'max_length': 'Name must be 100 characters or fewer.',
        },
    )

    price = forms.DecimalField(
        label='Price (USD)',
        max_digits=8,
        decimal_places=2,
        min_value=0.01,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '0.00',
            'step': '0.01',
        }),
        error_messages={
            'required': 'Please enter a price.',
            'min_value': 'Price must be greater than $0.00.',
            'invalid': 'Enter a valid number.',
        },
    )

    category = forms.ChoiceField(
        label='Category',
        choices=[
            ('', '— Select a category —'),
            ('Electronics', 'Electronics'),
            ('Books', 'Books'),
            ('Furniture', 'Furniture'),
            ('Accessories', 'Accessories'),
            ('Other', 'Other'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
        error_messages={
            'required': 'Please select a category.',
        },
    )

    description = forms.CharField(
        label='Description',
        required=False,
        max_length=300,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Brief product description (optional)…',
        }),
    )
