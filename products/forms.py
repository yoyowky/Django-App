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
    title       = forms.CharField(
                            max_length=120,
                            required=True,
                            widget=forms.TextInput({
                                "placeholder": "Your Title"
                            }))
    description = forms.CharField(
                            max_length=120,
                            required=True,
                            widget=forms.Textarea(attrs={
                                "placeholder": "Your Description",
                                "class": "new-class-name two",
                                "id": "my-id-for-textarea",
                                "rows": 20,
                                "col": 120

                            }))
    price       = forms.DecimalField(required=False)
    summary     = forms.CharField(max_length=120, required=False)
    featured    = forms.BooleanField(required=False)
