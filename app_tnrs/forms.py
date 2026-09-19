from django import forms
from .models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'description', 'image', 'is_available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'app-input'}),
            'price': forms.NumberInput(attrs={'class': 'app-input', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'app-input'}),
            'image': forms.ClearableFileInput(attrs={'class': ''}),
            'is_available': forms.CheckboxInput(attrs={}),
        }
