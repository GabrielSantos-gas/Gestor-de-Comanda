from django import forms

class ItemForm(forms.Form):
    descricao = forms.CharField(max_length=100)
    valor = forms.DecimalField(max_digits=10, decimal_places=2)
