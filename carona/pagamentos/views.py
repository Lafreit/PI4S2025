from django.shortcuts import render, redirect, get_object_or_404
from .models import Pagamento
from passageiros.models import SolicitacaoCarona
from .forms import PagamentoForm

def processar_pagamento(request, pk):
    solicitacao = get_object_or_404(SolicitacaoCarona, pk=pk)
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            pagamento = form.save(commit=False)
            pagamento.solicitacao_carona = solicitacao
            pagamento.status = 'processado'
            pagamento.save()
            return redirect('extrato_motorista')
    else:
        form = PagamentoForm()
    return render(request, 'pagamentos/processar_pagamento.html', {'form': form})

def extrato_motorista(request):
    pagamentos = Pagamento.objects.filter(solicitacao_carona__itinerario__motorista=request.user)
    return render(request, 'pagamentos/extrato_motorista.html', {'pagamentos': pagamentos})

def calcular_taxa(request):
    # Exemplo simples de cálculo
    taxa = 0.10  # 10%
    valor_base = 100  # exemplo
    valor_taxa = valor_base * taxa
    valor_motorista = valor_base - valor_taxa
    return render(request, 'pagamentos/calcular_taxa.html', {
        'valor_base': valor_base,
        'valor_taxa': valor_taxa,
        'valor_motorista': valor_motorista
    })