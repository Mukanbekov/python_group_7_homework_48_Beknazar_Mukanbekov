from django import forms

from products_app.models import Products


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'text', 'category', 'cost', 'remainder')


class ProductsDeleteForm(forms.Form):
    name = forms.CharField(max_length=120, required=True, label='Введите имя, чтобы удалить её')