from django import forms
from .models import Product
class ProductCreateForm(forms.ModelForm):
    title = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Enter the title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class":"new-class-name two","rows":20,"cols":50}))
    price = forms.DecimalField(initial=29.99)
    class Meta:
        model=Product
        fields=[
            'title','description','price'
        ]
    def clean_title(self,*args,**kwargs):
        title=self.cleaned_data.get('title')
        if not "raw" in title:
            raise forms.ValidationError("This is not a valid title")
        else:
            return title

class RawProductsForm(forms.Form):
    title = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Enter the title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class":"new-class-name two","rows":20,"cols":50}))
    price = forms.DecimalField(initial=29.99)