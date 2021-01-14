from django import forms

from .models import Product

# django model form
class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    email = forms.EmailField()
    discription = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
            "placeholder": "Your Discriiption",
            "class": "new-class-name two",
            "id": "my-id-for-textarea",
            "rows": 20,
            "cols": 120
        }))
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "news" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email
    


# django form, has validation
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
