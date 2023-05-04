from django import forms
from .models import Product
class ProductCreateForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=[
            'title','description','price'
        ]

class RawProductsForm(forms.Form):
    title = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Enter the title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class":"new-class-name two","rows":20,"cols":50}))
    price = forms.DecimalField(initial=29.99)