# pagamentos/forms.py
from django import forms
from .models import Pagamento

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['valor_total', 'taxa_app', 'valor_motorista', 'metodo_pagamento']