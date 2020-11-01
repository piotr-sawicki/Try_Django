from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'feature'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your title"
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "rows": 5,
                "cols": 20,
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
    feature = forms.BooleanField()
    summary = forms.CharField()
