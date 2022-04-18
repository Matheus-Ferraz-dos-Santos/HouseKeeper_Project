from django import forms
from django.forms import ModelForm
from .models import Quote
from django.utils.translation import gettext_lazy as _

class QuoteForm(ModelForm):
    required_css_class = 'required-field'
    error_css_class = 'error-field'
    class Meta:
        model = Quote
        fields = [
            'client_name', 'client_email', 'mobile', 'location_type', 'area_m2', 'qty_bedroom', 'qty_living', 'qty_bathroom', 'window', 'qty_window',
            'kitchen', 'kitchen_addon', 'bedroom_addon', 'living_addon','last_clean','pets', 'best_day', 'best_time', 'address'
        ]
        labels = {
        'client_name': _('Nome Completo'),
        'client_email':_('E-mail'),
        'window':_('Limpeza de janelas?')
        }
        widgets = {
            'client_name': forms.TextInput(attrs={'class':'form-control'}),
            'client_email':forms.EmailInput(attrs={'class':'form-control'}),
            'window':forms.CheckboxInput(),
            'kitchen_addon':forms.CheckboxSelectMultiple(attrs={'class': 'form-select'}),
            'bedroom_addon':forms.CheckboxSelectMultiple(attrs={'class': 'form-select'}),
            'living_addon':forms.CheckboxSelectMultiple(attrs={'option_inherits_attrs': True, 'class': 'form-select'}),

        }
