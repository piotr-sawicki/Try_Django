from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
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
    email = forms.EmailField()
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'feature'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not 'cfe' in title:
            raise forms.ValidationError("This is not a valid title!")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith('com'):
            raise forms.ValidationError("This is not a valid email!")
        return email



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
