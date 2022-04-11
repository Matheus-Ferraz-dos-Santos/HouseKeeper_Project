from django import forms
from django.forms import ModelForm
from .models import Quote

class QuoteForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Quote
        fields = [
            'client_name', 'client_email', 'mobile', 'location_type', 'area_m2', 'qty_bedroom', 'qty_living', 'qty_bathroom', 'window', 'qty_window',
            'kitchen', 'kitchen_addon', 'bedroom_addon', 'living_addon','last_clean','pets', 'best_day', 'best_time', 'address'
        ]
