from django import forms

from .models import Product

# django model form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


# django form
class RawProductForm(forms.Form):
    title       = forms.CharField(max_length=120, required=True)
    description = forms.CharField(max_length=120, required=True)
    price       = forms.DecimalField(required=False)
    summary     = forms.CharField(max_length=120, required=False)
    featured    = forms.BooleanField(required=False)
