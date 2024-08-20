from django import forms
from .models import Products


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'product_name': 'Product Name',
            'product_price': 'Product Price',
            'product_quantity': 'Product Quantity',
            'product_supplier': 'Product Supplier'
        }

        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder': 'Product ID', 'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'placeholder': 'Product Name', 'class': 'form-control'}),
            'product_price': forms.NumberInput(attrs={'placeholder': 'Product Price', 'class': 'form-control'}),
            'product_quantity': forms.NumberInput(attrs={'placeholder': 'Product Quantity', 'class': 'form-control'}),
            'product_supplier': forms.TextInput(attrs={'placeholder': 'Product Supplier', 'class': 'form-control'})

        }
