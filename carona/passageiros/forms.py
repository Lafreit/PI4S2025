# caronas/forms.py
from django import forms
from .models import Itinerario, SolicitacaoCarona

class ItinerarioForm(forms.ModelForm):
    class Meta:
        model = Itinerario
        fields = [
            'veiculo', 'origem', 'destino',
            'horario_saida', 'horario_chegada',
            'vagas_disponiveis', 'custo_por_passageiro'
        ]

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoCarona
        fields = []  # Se não houver campos editáveis pelo usuário, deixe vazio
